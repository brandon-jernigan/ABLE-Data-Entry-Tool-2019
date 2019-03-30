# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:27:53 2018
@author: Brandon Jernigan
Email: brandonjernigan@email.arizona.edu

Description: A script which allows for easier entry of data for uploading directly
into Tissue Metrix 2
"""

from datetime import datetime
from xml_generator import Generate_XML_File
import csv
import os
import pandas as pd
import sys
import time
import win32gui

global DEBUG_MODE
# DEBUG_MODE = True
DEBUG_MODE = False

global USER
USER = "Unknown"

global SCREEN_WIDTH
SCREEN_WIDTH = 121

global EFFECTIVE_SCREEN_WIDTH
EFFECTIVE_SCREEN_WIDTH = 120

global FIRST_FLAG
FIRST_FLAG = True

global FINAL_2ML_BOX_IN_RANGE
FINAL_2ML_BOX_IN_RANGE = 220
# FINAL_2ML_BOX_IN_RANGE = 27

global FINAL_4ML_BOX_IN_RANGE
FINAL_4ML_BOX_IN_RANGE = 300
# FINAL_4ML_BOX_IN_RANGE = 21

global EVENT_NAME_AND_SEQUENCE_SAME
EVENT_NAME_AND_SEQUENCE_SAME = True
# global DEF_SERUM
# DEF_SERUM = 5
# global NUM_SERUM
# NUM_SERUM = DEF_SERUM
#
# global DEF_PLASMA
# DEF_PLASMA = 6
# global NUM_PLASMA
# NUM_PLASMA = DEF_PLASMA
#
# global DEF_PBMC
# DEF_PBMC = 1
# global NUM_PBMC
# NUM_PBMC = DEF_PBMC
#
# global DEF_PAXGENE
# DEF_PAXGENE = 2
# global NUM_PAXGENE
# NUM_PAXGENE = DEF_PAXGENE

global DEVICE
DEVICE = "ABLE 008"

global SHELF_2ML
SHELF_2ML = "Shelf2"

global SHELF_4ML
SHELF_4ML = "Shelf3"


def main():
    if not DEBUG_MODE:
        Launch()
    Title()
    User()
    print("\n")
    menu_flag = True
    more_donors_flag = False
    continue_response = None
    redo = False
    donor_list = []
    while True:
        if menu_flag:
            menu_response = Menu()
            import_package_name = ""

        Set_defaults()
        complete = "n"
        new_master = False

        file_location = os.path.join(
            os.pardir, "Collections", "CDDOM", "Master", "CDDOM.csv"
        )

        if os.path.exists(file_location):

            current_data = pd.read_csv(file_location)
        else:
            response = input("No master file found, create a new one?(y/n): ")
            if response == "y":
                new_master = True
                current_data = None
            else:
                print(
                    "\nProgram cannot execute without a master file.\nExiting", end=""
                )
                Dot_Dot_Dot()
                sys.exit()

        first_flag = True
        while complete == "n":

            form = {
                "donor_ID": "",
                "event_sequence": "001",
                "event_name": "001",
                "sample_number": "",
                "study_ID": "",
                "event_date": DATE,
                "event_time": TIME,
                "sample_class": "",
                "sample_type": "",
                "storage_device": DEVICE,
                "storage_shelf": "",
                "storage_box": "",
                "storage_slot": "",
            }
            #            os.system('color f1')
            Collection_Title(menu_response)

            if complete == "n" and not first_flag:
                print("Redo", end="")
                Dot_Dot_Dot()

            if not more_donors_flag and not redo:
                sample_list = CDDOM_Submenu(menu_response, form)
            if redo or more_donors_flag:
                sample_list = CDDOM_Register_Prompt(menu_response, form)
                redo = False
            #            sample_list = CDDOM_Prompt(menu_response, form)
            if sample_list:
                sample_list = Determine_sample_locations(
                    current_data, sample_list, new_master
                )
                if len(sample_list) > 0:
                    complete, sample_list = Confirm(sample_list)
                    if complete == "n":
                        redo = True
                else:
                    print("No Samples entered, Redo", end="")
                    Dot_Dot_Dot()
                    complete = "n"
                first_flag = False
            else:
                menu_flag = True
                complete = "y"
        if sample_list:
            import_package_name_new = Write_new_data(
                sample_list, import_package_name, new_master
            )

            import_package_name = import_package_name_new
            complete_2 = "n"
            donor_list.append(form["donor_ID"])
            while complete_2 == "n":

                print("\n\nDonors registered:\n")
                for ii, ID in enumerate(donor_list):
                    if ii % 5 == 0 and ii != 0:
                        print()
                    print(ID, end="  ")

                continue_response = input(
                    "\n\nPress 'Enter' to continue making entries in this collection, or press 'i' to finish generating import package: "
                ).lower()
                if continue_response == "i" or continue_response == "":
                    complete_2 = "y"

            if continue_response == "i":
                print("\nCreating import package", end="")
                Dot_Dot_Dot()
                menu_flag = True
                more_donors_flag = False
                donor_list = []

                import_package_folder = os.path.join(
                    os.pardir, "Import Packages", "CSVs"
                )
                if not os.path.exists(import_package_folder):
                    os.makedirs(import_package_folder)

                import_package_file_path = os.path.join(
                    import_package_folder, import_package_name
                )
                Generate_XML_File(import_package_file_path, "back")

            else:
                menu_flag = False
                first_flag = False
                more_donors_flag = True
                print("\n")


def Launch():
    os.system("cls")
    os.system("mode con: cols=100 lines=1000")
    hwnd = win32gui.GetForegroundWindow()
    win32gui.MoveWindow(hwnd, 450, 0, 0, 0, True)
    os.system("mode con: cols=%s lines=500" % SCREEN_WIDTH)


def Title():
    os.system("cls")
    os.system("color 0f")
    #    with open("snowflake.txt", 'r') as read_file:
    #        snowflake_lines = read_file.readlines()

    with open("snowflake_inv.txt", "r") as read_file:
        snowflake_inv_lines = read_file.readlines()

    with open("title.txt", "r") as read_file:
        title_lines = read_file.readlines()

    #    secs = 0.033

    for line in snowflake_inv_lines:
        print(line, end="")

    #    for num in range(4):
    #        time.sleep(secs)
    #        os.system("cls")
    #
    #        for line in snowflake_inv_lines:
    #            print(line, end = '')
    #
    #        time.sleep(secs)
    #        os.system("cls")
    #
    #        for line in snowflake_lines:
    #            print(line, end = '')
    for line in title_lines:
        print(line, end="")


def User():
    Title()
    complete = "n"
    while complete == "n":
        response = input("\nUser Initials: ")
        if response != "":
            global USER
            USER = response
            complete = "y"
        else:
            print("Try again")


def Menu():
    Title()

    print("\n  1) CDDOM (AT)\t\t\t  3) H3 Africa (coming soon)")
    print("  2) Saliva (coming soon)\t  x) Exit")
    #    print("  3) test\t  o) test")
    #    print("  4) test\t  x) test")
    loop = True
    while loop:
        loop = False
        response = input("\nPlease make a selection: ")

        if response == "1":
            collection = "CDDOM Collection (AT)"

        elif response.lower() == "x":
            print("\nExiting", end="")
            Dot_Dot_Dot()
            sys.exit()
        else:
            print("Try again")
            loop = True

    return collection


def Dot_Dot_Dot(seconds_between=0.3):
    sys.stdout.flush()
    time.sleep(seconds_between)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(seconds_between)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(seconds_between)
    print(".", end="")
    sys.stdout.flush()
    time.sleep(seconds_between * 1.5)


def Print_Star_Line():
    for num in range(EFFECTIVE_SCREEN_WIDTH):
        print("*", end="")
    print("")


def Print_Centered_Line(string):
    num_spaces = (EFFECTIVE_SCREEN_WIDTH - len(string)) // 2

    for num in range(num_spaces):
        print(" ", end="")

    print(string)


def Collection_Title(collection, clear_screen=True, end_space=True):

    if clear_screen:
        os.system("cls")

    #    with open("special_snowflake1.txt", 'r') as read_file:
    #        snowflake = read_file.readlines()
    #
    #    print('')
    #
    #    for line in snowflake:
    #        Print_Centered_Line(line.rstrip())

    Print_Star_Line()
    Print_Centered_Line(collection)
    Print_Star_Line()

    if end_space:
        print("\n")


def Set_defaults():
    global DATE
    DATE = datetime.now().strftime("%m-%d-%Y")

    global TIME
    TIME = datetime.now().strftime("%H:%M")

    global TIME_FULL
    TIME_FULL = datetime.now().strftime("%m-%d-%Y   %Hh %Mm %Ss")

    global DEF_SERUM
    DEF_SERUM = 5
    global NUM_SERUM
    NUM_SERUM = DEF_SERUM

    global DEF_PLASMA
    DEF_PLASMA = 6
    global NUM_PLASMA
    NUM_PLASMA = DEF_PLASMA

    global DEF_PBMC
    DEF_PBMC = 1
    global NUM_PBMC
    NUM_PBMC = DEF_PBMC

    global DEF_PAXGENE
    DEF_PAXGENE = 2

    global NUM_PAXGENE
    NUM_PAXGENE = DEF_PAXGENE

    global COLLECTION_NAME
    COLLECTION_NAME = "CDDOM"


def CDDOM_Submenu(menu_response, form):
    """
    CDDOM_Submenu [summary]

    [description]

    Arguments:
        menu_response {[type]} -- [description]
        form {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    loop = True
    while loop:
        Title()
        Collection_Title(menu_response, clear_screen=False, end_space=False)

        print(
            "  1) Reserve Kit IDs\t\t\t  2) Register Samples\t\t  m) Return to Main Menu"
        )
        loop = False
        response = input("\nPlease make a selection: ")

        if response == "1":
            sample_list = CDDOM_Generate_New_IDs(menu_response)
            loop = True

        elif response == "2":
            sample_list = CDDOM_Register_Prompt(menu_response, form)

        elif response.lower() == "m":
            return False
        else:
            print("Try again")
            Dot_Dot_Dot()
            loop = True

    return sample_list


# def CDDOM_Kit_Prompt(menu_response, form):
#
#    loop = True
#    while loop:
#        Title()
#        Collection_Title(menu_response, clear_screen = False, end_space = False)
#        print("  1) Generate new IDs\t\t\t   m) Return to Menu")
#        loop = False
#        response_m = input("\nPlease make a selection: ")
#
#        if response_m == "1":
#            loop = CDDOM_Generate_New_IDs(menu_response)
#            loop = True
# elif response_m == "2":
##            complete = 'n'
# while complete == 'n':
##                response = input("Donor ID (AT): ")
# if len(response) == 11:
##                    complete = 'y'
# else:
##                    print("Try again")
#
#        elif response_m.lower() == 'm':
#            return None
#        else:
#            print("Try again")
#            Dot_Dot_Dot()
#            loop = True
#
#    return None


def CDDOM_Generate_New_IDs(menu_response):
    main_complete = "n"
    while main_complete == "n":
        reserved_IDs_folder = os.path.join(
            os.pardir, "Collections", COLLECTION_NAME, "Master"
        )
        reserved_IDs_path = os.path.join(reserved_IDs_folder, "Reserved_IDs.csv")
        Collection_Title(menu_response)

        if not os.path.exists(reserved_IDs_folder):
            os.makedirs(reserved_IDs_folder)

        results = []
        try:
            with open(reserved_IDs_path, newline="") as inputfile:
                for row in csv.reader(inputfile):
                    for item in row:
                        if item != "":
                            results.append(item)
            if results[-1] != "":
                last_ID = results[-1]
            else:
                complete = "n"
                while complete == "n":
                    last_ID = input(
                        "No file found, please enter last used donor ID (AT): "
                    )
                    if len(last_ID) == 11 and " " not in last_ID:
                        complete = "y"
                    else:
                        print("Try again")
                print()

        except:
            open(reserved_IDs_path, "a").close()
            complete = "n"
            while complete == "n":
                last_ID = input("No file found, please enter last used donor ID (AT): ")
                if len(last_ID) == 11 and " " not in last_ID:
                    complete = "y"
                else:
                    print("Try again")
            print()

        complete = "n"
        while complete == "n":
            print("Last used ID was %s\n" % last_ID)
            response = input("Generate how many sequential donor IDs?: ")

            if len(response) < 4 and response.isdigit():
                complete = "y"
            else:
                print("Try again")

        last_ID_end = last_ID.split("-")[2].lstrip()

        if int(last_ID_end) + int(response) >= 100000:
            print("Ran out of numbers")
            Dot_Dot_Dot()
            return False
        ID_list = []
        indices = {}
        for num in range(int(response)):
            indices[num] = num + 1
            new_ID_end = int(last_ID_end) + 1
            new_ID = "AT-01-" + str(new_ID_end).rjust(5, "0")

            ID_list.append(new_ID)

            last_ID_end = new_ID_end

        print("\nPlease confirm whether this information is correct:\n")
        for ii, ID in enumerate(ID_list):
            if ii % 5 == 0 and ii != 0:
                print()
            print(ID, end="  ")

        correct = None
        while correct == None:
            correct = input("\n\nIs this correct (y/n)?: ").lower()
            if correct == "y":
                main_complete = "y"
            else:
                print("Try again", end="")
                Dot_Dot_Dot()

    print("\nReserving donor IDs", end="")
    Dot_Dot_Dot()

    with open(reserved_IDs_path, "a", newline="") as write_file:

        writer = csv.writer(write_file)

        writer.writerow(ID_list)

    with open(
        os.path.join(reserved_IDs_folder, "Most_Recent_ID_Reservations.txt"), "w"
    ) as write_file_2:
        for line in ID_list:
            write_file_2.write("%s\n" % line)

    os.system(
        "start " + os.path.join(reserved_IDs_folder, "Most_Recent_ID_Reservations.txt")
    )

    return False


def CDDOM_Register_Prompt(menu_response, form):

    Collection_Title(menu_response)

    #    Enter_input('alphanum', "Donor ID: ", form["donor_ID"], False, length = 11)

    complete = "n"
    while complete == "n":
        form["donor_ID"] = input("Donor ID (AT): ")
        #        form["donor_ID"] = "AT-01-00214"
        if len(form["donor_ID"]) == 11 and " " not in form["donor_ID"]:
            complete = "y"
        else:
            print("Try again")

    #    Enter_input('alphanum', "Study ID: ", form["study_ID"], False, length = 10)

    complete = "n"
    while complete == "n":
        form["study_ID"] = input("\nStudy ID: ")
        #        form["study_ID"] = "01-0094-01"
        if len(form["study_ID"]) == 10:
            complete = "y"
        else:
            print("Try again")

    #    Enter_input('alphanum', "Event (press enter for '001'): ", form["event_date"], True, length = 3)
    complete = "n"
    while complete == "n":
        response = input("\nEvent ID (press enter for '001'): ")
        if response == "":
            complete = "y"
        elif len(response) == 3:
            form["event_name"] = response
            complete = "y"
        else:
            print("Try again")

    if not EVENT_NAME_AND_SEQUENCE_SAME:
        complete = "n"
        while complete == "n":
            response = input("\nEvent Sequence (press enter for '001'): ")
            if response == "":
                complete = "y"
            elif len(response) == 3:
                form["event_sequence"] = response
                complete = "y"
            else:
                print("Try again")
    else:
        form["event_sequence"] = form["event_name"]

    #    Enter_input('alphanum', "Event date (in MM-DD-YYYY format, press enter for '%s'): " % DATE, form["event_date"], True, length = 10)

    complete = "n"
    while complete == "n":
        response = input(
            "\nEvent date (in MM-DD-YYYY format, press enter for '%s'): " % DATE
        )
        if response == "":
            complete = "y"
        elif len(response) == 10:
            form["event_date"] = response
            form["event_time"] = "12:00:00"
            complete = "y"
        else:
            print("Try again")

    Enter_input("num", "\nNumber of serum vials (press enter for '5'): ", "serum", True)

    #    complete = 'n'
    #    while complete == 'n':
    #        response = input("Number of serum vials (press enter for '5'): ")
    #        if response == '':
    #            complete = 'y'
    #        elif response.isdigit():
    #            NUM_SERUM = response
    #            complete = 'y'

    Enter_input(
        "num", "\nNumber of plasma vials (press enter for '6'): ", "plasma", True
    )

    #    complete = 'n'
    #    while complete == 'n':
    #        response = input("Number of plasma vials (press enter for '6'): ")
    #        if response == '':
    #            complete = 'y'
    #        elif response.isdigit():
    #            NUM_PLASMA = response
    #            complete = 'y'

    Enter_input(
        "num", "\nNumber of Molecular PBMC vials (press enter for '1'): ", "PBMC", True
    )

    #    complete = 'n'
    #    while complete == 'n':
    #        response = input("Number of Molecular PBMC vials (press enter for '1'): ")
    #        if response == '':
    #            complete = 'y'
    #        elif response.isdigit():
    #            NUM_PBMC = response
    #            complete = 'y'

    Enter_input(
        "num", "\nNumber of PAXgene vials (press enter for '2'): ", "PAXgene", True
    )

    #    complete = 'n'
    #    while complete == 'n':
    #        response = input("Number of PAXgene vials (press enter for '2'): ")
    #        if response == '':
    #            complete = 'y'
    #        elif response.isdigit():
    #            NUM_PAXGENE = response
    #            complete = 'y'

    sample_list = Convert_vials_to_entries(form)

    return sample_list


def Enter_input(q_type, question, sample_type, has_default, length="0"):
    complete = "n"
    while complete == "n":
        response = input(question)
        if response == "" and has_default:
            complete = "y"
        elif q_type == "num" and response.isdigit():
            if sample_type == "serum":
                global NUM_SERUM
                NUM_SERUM = int(response)
            if sample_type == "plasma":
                global NUM_PLASMA
                NUM_PLASMA = int(response)
            if sample_type == "PBMC":
                global NUM_PBMC
                NUM_PBMC = int(response)
            if sample_type == "PAXgene":
                global NUM_PAXGENE
                NUM_PAXGENE = int(response)
            complete = "y"
        #        elif q_type == 'alphanum' and len(response) == length:
        #            variable = response
        #            complete = 'y'
        #            return response
        else:
            print("Try Again")


def Convert_vials_to_entries(form):
    sample_list = []
    count = 0

    for sample in range(NUM_SERUM):
        line = form.copy()
        count += 1
        line["sample_class"] = "Fluid"
        line["sample_type"] = "SERUM"
        line["sample_number"] = ("%s" % count).zfill(3)
        line["storage_shelf"] = SHELF_2ML

        sample_list.append(line)

    for sample in range(NUM_PLASMA):
        line = form.copy()
        count += 1
        line["sample_class"] = "Fluid"
        line["sample_type"] = "PLASMA"
        line["sample_number"] = ("%s" % count).zfill(3)
        line["storage_shelf"] = SHELF_2ML

        sample_list.append(line)

    for sample in range(NUM_PBMC):
        line = form.copy()
        count += 1
        line["sample_class"] = "Molecular"
        line["sample_type"] = "BUFFY (PBMC)"
        line["sample_number"] = ("%s" % count).zfill(3)
        line["storage_shelf"] = SHELF_2ML

        sample_list.append(line)

    for sample in range(NUM_PAXGENE):
        line = form.copy()
        count += 1
        line["sample_class"] = "Molecular"
        line["sample_type"] = "PAXGENE"
        line["sample_number"] = ("%s" % count).zfill(3)
        line["storage_shelf"] = SHELF_4ML

        sample_list.append(line)

    return sample_list


def Determine_sample_locations(current_data, sample_list, new_master):

    if new_master:
        complete = "n"
        while complete == "n":
            print("\n\nI need to determine where to store these.")
            prev_box_2ml = input("What is the last occupied 2ml box number?: ")
            prev_position_2ml = input("What is the last occupied 2ml slot number?: ")

            prev_box_4ml = input("What is the last occupied PAXgene box number?: ")
            prev_position_4ml = input(
                "What is the last occupied PAXgene slot number?: "
            )

            prev_pattern_4ml = input(
                "\nI need more information to store PAXgene vials. PAXgene vials are stored in groups of 3 with gaps in between.\nHow many PAXgene vials in a row are in the most recent storage, before the nearest gap? (1, 2, or 3): "
            )
            if (
                prev_box_2ml != ""
                and prev_position_2ml != ""
                and prev_box_4ml != ""
                and prev_position_4ml != ""
                and prev_pattern_4ml != ""
            ):
                complete = "y"

        prev_box_2ml = int(prev_box_2ml)
        prev_position_2ml = int(prev_position_2ml)
        prev_box_4ml = int(prev_box_4ml)
        prev_position_4ml = int(prev_position_4ml)
        prev_pattern_4ml = int(prev_pattern_4ml)

    else:

        PAXgene_data = current_data.loc[current_data["Sample Type"] == "PAXGENE"]
        non_PAXgene_data = current_data.loc[current_data["Sample Type"] != "PAXGENE"]

        non_PAXgene_data_last_entry = non_PAXgene_data.iloc[-1]

        prev_box_2ml = int(
            non_PAXgene_data_last_entry["Storage Address"].split("-")[-2][3:]
        )
        prev_position_2ml = int(
            non_PAXgene_data_last_entry["Storage Address"].split("-")[-1]
        )

        if PAXgene_data.shape[0] >= 3:

            PAXgene_box_positions = [
                int(PAXgene_data.iloc[-1]["Storage Address"].split("-")[-1]),
                int(PAXgene_data.iloc[-2]["Storage Address"].split("-")[-1]),
                int(PAXgene_data.iloc[-3]["Storage Address"].split("-")[-1]),
            ]

            test_1 = PAXgene_box_positions[0] - PAXgene_box_positions[2]
            if test_1 < 0:
                test_1 = PAXgene_box_positions[0] - (PAXgene_box_positions[2] - 81)
            test_2 = PAXgene_box_positions[1] - PAXgene_box_positions[2]
            if test_2 < 0:
                test_2 = PAXgene_box_positions[1] - (PAXgene_box_positions[2] - 81)

            if test_1 == 2:
                prev_pattern_4ml = 3
            elif test_1 == 3 and test_2 == 2:
                prev_pattern_4ml = 2
            else:
                prev_pattern_4ml = 1

            prev_box_4ml = int(
                PAXgene_data.iloc[-1]["Storage Address"].split("-")[-2][3:]
            )
            prev_position_4ml = int(
                PAXgene_data.iloc[-1]["Storage Address"].split("-")[-1]
            )

        else:
            if PAXgene_data.shape[0] >= 1:
                prev_box_4ml = int(
                    PAXgene_data.iloc[-1]["Storage Address"].split("-")[-2][3:]
                )
                prev_position_4ml = int(
                    PAXgene_data.iloc[-1]["Storage Address"].split("-")[-1]
                )

            complete = "n"
            while complete == "n":
                prev_pattern_4ml = input(
                    "\nI need more information to store PAXgene vials. PAXgene vials are stored in groups of 3 with gaps in between.\nHow many PAXgene vials in a row are in the most recent storage, before the nearest gap? (1, 2, or 3): "
                )
                if PAXgene_data.shape[0] == 0:
                    prev_box_4ml = input(
                        "What is the last occupied PAXgene box number?: "
                    )
                    prev_position_4ml = input(
                        "What is the last occupied PAXgene slot number?: "
                    )
                if (
                    prev_pattern_4ml != ""
                    and prev_box_4ml != ""
                    and prev_position_4ml != ""
                ):
                    complete = "y"
            prev_pattern_4ml = int(prev_pattern_4ml)

    num_2ml = 0

    for line in sample_list:
        if line["sample_type"] != "PAXGENE":
            num_2ml += 1

    if (
        num_2ml != 0
        and (
            (
                (len(sample_list) + prev_position_2ml) > 81
                and (len(sample_list) / 81 + prev_box_2ml) >= FINAL_2ML_BOX_IN_RANGE
            )
            or (prev_position_2ml >= 81 and prev_box_2ml + 1 >= FINAL_2ML_BOX_IN_RANGE)
        )
    ) or prev_box_2ml >= FINAL_2ML_BOX_IN_RANGE + 1:

        print(
            "Last box in 2ml storage range reached, please find a new location to store these samples. Exiting",
            end="",
        )
        Dot_Dot_Dot()
        sys.exit()

    num_4ml = 0

    for line in sample_list:
        if line["sample_type"] == "PAXGENE":
            num_4ml += 1

    if (
        num_4ml != 0
        and (
            (
                (len(sample_list) + 1 + prev_position_4ml) > 81
                and (len(sample_list) / 81 + prev_box_4ml) >= FINAL_4ML_BOX_IN_RANGE
            )
            or (prev_position_4ml >= 79 and prev_box_4ml + 1 >= FINAL_4ML_BOX_IN_RANGE)
        )
    ) or prev_box_4ml >= FINAL_4ML_BOX_IN_RANGE + 1:

        print(
            "Last box in 4ml storage range reached, please find a new location to store these samples. Exiting",
            end="",
        )
        Dot_Dot_Dot()
        sys.exit()

    for line in sample_list:

        if line["sample_type"] == "PAXGENE":

            if prev_pattern_4ml == 3:
                pattern_4ml = 1
            elif prev_pattern_4ml == 1:
                pattern_4ml = 2
            else:
                pattern_4ml = 3

            if prev_position_4ml >= 81:
                box_4ml = prev_box_4ml + 1
                prev_position_4ml = 0
            elif prev_position_4ml == 80 and pattern_4ml == 1:
                box_4ml = prev_box_4ml + 1
                prev_position_4ml = -1
            else:
                box_4ml = prev_box_4ml

            if pattern_4ml == 1:
                position_4ml = prev_position_4ml + 2
            else:
                position_4ml = prev_position_4ml + 1

            line["storage_box"] = "Box%s" % box_4ml
            line["storage_slot"] = ("%s" % position_4ml).zfill(3)

            prev_position_4ml = position_4ml
            prev_box_4ml = box_4ml
            prev_pattern_4ml = pattern_4ml
        else:

            if prev_position_2ml >= 81:
                box_2ml = prev_box_2ml + 1
                prev_position_2ml = 0
            else:
                box_2ml = prev_box_2ml

            position_2ml = prev_position_2ml + 1

            line["storage_box"] = "Box%s" % box_2ml
            line["storage_slot"] = ("%s" % position_2ml).zfill(3)

            prev_position_2ml = position_2ml
            prev_box_2ml = box_2ml

    return sample_list


def Confirm(sample_list):

    new_string = ""
    correct = None

    print("\n\nPlease confirm whether this information is correct:\n")

    print(
        "Sample Number\t\tStudy ID\tEvent Date\tSample Class\tSample Type\tStorage Address"
    )

    for num, line in enumerate(sample_list):

        if len(line["sample_class"]) <= 8 and len(line["sample_type"]) <= 8:
            string_format = "%s-%s-%s\t%s\t%s\t%s\t\t%s\t\t%s-%s-%s-%s"
        elif len(line["sample_class"]) <= 8:
            string_format = "%s-%s-%s\t%s\t%s\t%s\t\t%s\t%s-%s-%s-%s"
        elif len(line["sample_type"]) <= 8:
            string_format = "%s-%s-%s\t%s\t%s\t%s\t%s\t\t%s-%s-%s-%s"
        else:
            string_format = "%s-%s-%s\t%s\t%s\t%s\t%s\t%s-%s-%s-%s"

        print(
            string_format
            % (
                line["donor_ID"],
                line["event_sequence"],
                line["sample_number"],
                line["study_ID"],
                line["event_date"],
                line["sample_class"],
                line["sample_type"],
                line["storage_device"],
                line["storage_shelf"],
                line["storage_box"],
                line["storage_slot"],
            )
        )

    while correct == None:
        correct = input("%s\nIs this correct (y/n)?: " % new_string).lower()

        if correct == "y":

            complete = "y"
            return complete, sample_list

        elif correct == "n":

            print("Redo\n")
            complete = "n"
            return complete, sample_list

        else:

            new_string = "\nTry again.\n"
            correct = None


def Write_new_data(sample_list, import_package_name, new_master):

    print("\nWriting to file", end="")
    Dot_Dot_Dot()
    collection = "CDDOM"
    folder_collections = "Collections"
    import_folder = "Import Packages"
    folder_master = "Master"
    folder_CSVs = "Donor_CSVs"
    file_name = "%s-%s" % (sample_list[0]["donor_ID"], sample_list[0]["event_sequence"])

    full_folder = os.path.join(
        os.pardir, folder_collections, COLLECTION_NAME, folder_CSVs, file_name
    )
    import_package_folder = os.path.join(os.pardir, import_folder, "CSVs")
    master_folder = os.path.join(
        os.pardir, folder_collections, COLLECTION_NAME, folder_master
    )

    csv_file_name = "%s.csv" % file_name

    if import_package_name == "":
        first_import = True
        import_package_name = "%s   %s.csv" % (collection, TIME_FULL)
    else:
        first_import = False

    master_file_name = "%s.csv" % COLLECTION_NAME
    html_file_name = "%s.html" % file_name

    file_path = os.path.join(full_folder, csv_file_name)
    import_package_path = os.path.join(import_package_folder, import_package_name)
    master_path = os.path.join(master_folder, master_file_name)

    if not os.path.exists(full_folder):
        os.makedirs(full_folder)

    if not os.path.exists(import_package_folder):
        os.makedirs(import_package_folder)

    if not os.path.exists(master_folder):
        os.makedirs(master_folder)

    try:
        with open(file_path, "w", newline="") as write_file, open(
            import_package_path, "a", newline=""
        ) as write_import, open(master_path, "a", newline="") as write_file_master:

            item_list_list = []

            writer = csv.writer(write_file)
            writer_import = csv.writer(write_import)
            writer_master = csv.writer(write_file_master)

            label_list = []

            label_list.append("Donor")
            label_list.append("Event Sequence")
            label_list.append("Event Name")
            label_list.append("Sample Number")
            label_list.append("Study ID")
            label_list.append("Sample Class")
            label_list.append("Sample Type")
            label_list.append("Storage Address")
            label_list.append("Event Date")
            label_list.append("Event Time")
            label_list.append("Registration Date")
            label_list.append("Registration Time")
            label_list.append("Storage Status")
            label_list.append("Inventory Status")
            label_list.append("Donor Comment")
            label_list.append("Event Comment")
            label_list.append("Sample Comment")
            label_list.append("Entered By")

            writer.writerow(label_list)

            if new_master:
                writer_master.writerow(label_list)
            if first_import:
                writer_import.writerow(label_list)

            indices = {}

            for num, line in enumerate(sample_list):

                indices[num] = num + 1
                item_list = []

                sample_num = "%s-%s-%s" % (
                    line["donor_ID"],
                    line["event_sequence"],
                    line["sample_number"],
                )

                location = "%s-%s-%s-%s" % (
                    line["storage_device"],
                    line["storage_shelf"],
                    line["storage_box"],
                    line["storage_slot"],
                )

                item_list.append(line["donor_ID"])
                item_list.append(line["event_sequence"])
                item_list.append(line["event_name"])
                item_list.append(sample_num)
                item_list.append(line["study_ID"])
                item_list.append(line["sample_class"])
                item_list.append(line["sample_type"])
                item_list.append(location)
                item_list.append(line["event_date"])
                item_list.append(line["event_time"])
                item_list.append(DATE)
                item_list.append(TIME)
                item_list.append("Available")
                item_list.append("IN")
                item_list.append("")
                item_list.append("")
                item_list.append("")
                if num == 0:
                    item_list.append(USER)
                elif num == 1:
                    item_list.append(DATE)
                elif num == 2:
                    item_list.append(TIME)
                else:
                    item_list.append("")

                item_list_list.append(item_list)

                writer.writerow(item_list)
                writer_master.writerow(item_list)
                writer_import.writerow(item_list)

            data_frame = pd.DataFrame(item_list_list, columns=label_list)
            data_frame = data_frame.drop(
                [
                    "Donor",
                    "Event Sequence",
                    "Event Name",
                    "Event Sequence",
                    "Event Time",
                    "Registration Date",
                    "Registration Time",
                    "Storage Status",
                    "Inventory Status",
                    "Donor Comment",
                    "Event Comment",
                    "Sample Comment",
                ],
                axis=1,
            )

            data_frame = data_frame.rename(index=indices)

            #            print(data_frame)

            data_frame.to_html(os.path.join(full_folder, html_file_name))
            os.system("start " + os.path.join(full_folder, html_file_name))

        Generate_XML_File(file_path, "same")
    except:
        print(
            "An error occured, please make sure all files related to this program are closed and try again."
        )

    return import_package_name


if __name__ == "__main__":
    main()
