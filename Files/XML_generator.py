# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 00:24:33 2018

@author: Brandon
Email: brandonjernigan@email.arizona.edu

Description: A script for the ANLE Data Entry Tool which parses a csv file to an xml
file in a format that allows the samples it contains to be imported into tissue metrix
"""



import os
import sys
from lxml import etree
import pandas as pd


    
    
def Generate_XML_File(file_path, folder_type):

    sample_info = pd.read_csv(file_path, dtype=str).fillna('')
#    donor_number = "9900074"
#    donor_comments = ''
#    
#    event_name = "001"
#    event_date = "2018-10-14T11:21:00"
#    event_sequence = "001"
#    
#    sample_number = "9900074-001-001"
#    storage_address = "ABLE 001-Shelf1-Box6-072"
#    sample_type = "Fluid"
#    sample_prep = "PLASMA"
#    storage_status = "Available"
#    inventory_status = "IN" 
    
    num_rows = len(sample_info.index)
    row = 0
    
    attr_qname_sch = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    attr_qname_nil = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "nil")
    
    import_package = etree.Element('IMPORT_PACKAGE', {attr_qname_sch: "https://tmx.uahs.arizona.edu:8443/extras/tmx2-import.xsd"}, 
                            nsmap = {"xsi": "http://www.w3.org/2001/XMLSchema-instance"})
    donors = 0
    donor_package = []
    
    #need to create unique branch names using a list, all samples are being added to the same branch
    while row < num_rows:       
        donors += 1
        donor_number = sample_info['Donor'][row]
        study_ID = sample_info['Study ID'][row]
        donor_comments = sample_info['Donor Comment'][row]
        
        date_registered = sample_info['Registration Date'][row]
        date_registered = "%s-%s-%s" % (date_registered.split('-')[2], date_registered.split('-')[0], date_registered.split('-')[1])
        time_registered = sample_info['Registration Time'][row]
        date_time_registered = "%sT%s:00" % (date_registered, time_registered)
        
        donor_package.append(etree.SubElement(import_package, "DONOR_PACKAGE"))
        
        donor = etree.SubElement(donor_package[donors - 1], "DONOR")
        
        
        
        donor_attributes = ["DONOR_NUMBER", "SOURCE1", "FILE1", "CONTACT1", "SOURCE2", "FILE2",
                            "CONTACT2", "SOURCE3", "FILE3", "CONTACT3", "FIRST_NAME", "MIDDLE_NAME",
                            "LAST_NAME", "DATE_OF_BIRTH", "PLACE_OF_BIRTH", "SEX", "SPECIES",
                            "PAT_ETHNICITY", "MAT_ETHNICITY", "DISEASE_CODE", "DISEASE_SITE", 
                            "DATE_REGISTERED", "ADDRESS1", "ADDRESS2", "CITY", "STATE", "COUNTRY",
                            "POSTAL_CODE", "TELEPHONE_HOME", "TELEPHONE_BUS", "DONOR_STATUS", 
                            "DATE_LAST_FUP", "DATE_NEXT_FUP", "DATE_OF_DEATH", "CAUSE_OF_DEATH", "COMMENTS"]
        
        for attribute in donor_attributes:
            if attribute == "DONOR_NUMBER":
                etree.SubElement(donor, attribute).text = donor_number
            elif attribute == "COMMENTS" and donor_comments != '':
                etree.SubElement(donor, attribute).text = donor_comments
            elif attribute == "DATE_REGISTERED" and date_time_registered != '':
                etree.SubElement(donor, attribute).text = date_time_registered
            elif attribute == "FIRST_NAME" and study_ID != '':
                etree.SubElement(donor, attribute).text = study_ID
            else:
                etree.SubElement(donor, attribute, {attr_qname_nil: "true"})
        
        
        
        events = 0
        event = []
        event_package = []
        
        while sample_info['Donor'][row] == donor_number:
            
            events += 1
            
            event_name = sample_info['Event Name'][row]
            event_sequence = sample_info['Event Sequence'][row] 
            
            event_date = sample_info['Event Date'][row]
            event_date = "%s-%s-%s" % (event_date.split('-')[2], event_date.split('-')[0], event_date.split('-')[1])
            event_time = sample_info['Event Time'][row]
            event_date_time = "%sT%s:00" % (event_date, event_time)
            
                    
            
            event_package.append(etree.SubElement(donor_package[donors - 1], "EVENT_PACKAGE"))
            
            event.append(etree.SubElement(event_package[events - 1], "EVENT"))
            
            sample_package = etree.SubElement(event_package[events - 1], "SAMPLE_PACKAGE")
            
            event_attributes = ["EVENT_NAME", "EVENT_DATE", "EVENT_SEQUENCE", "PERFORMANCE", "DONOR_HEIGHT", "DONOR_WEIGHT",
                                "DONOR_BSA", "HEMOGLOBIN", "DISEASE_SITE", "DISEASE_CODE", "PATHOLOGY", "SURGERY",
                                "SYS_THERAPY", "RADIATION", "TOXICITY", "OUTCOMES", "PATIENT_HX", "FAMILY_HX",
                                "NEO_ADJ_TREAT", "CLINICAL_TRIAL", "TRIAL_NAME", "TRIAL_SPONSOR", "PROG_DATE", "PROG_STATUS",
                                "PROG_SITE", "COMMENTS"]
            
            for attribute in event_attributes:
                if attribute == "EVENT_NAME":
                    etree.SubElement(event[events -1], attribute).text = event_name
                elif attribute == "EVENT_DATE" and event_date_time != '':
                    etree.SubElement(event[events -1], attribute).text = event_date_time
                elif attribute == "EVENT_SEQUENCE":
                    etree.SubElement(event[events -1], attribute).text = event_sequence
                else:
                    etree.SubElement(event[events -1], attribute, {attr_qname_nil: "true"})
            
            
            
            while sample_info['Event Name'][row] == event_name and sample_info['Donor'][row] == donor_number:
                
                sample_number = sample_info['Sample Number'][row]
                storage_address = sample_info['Storage Address'][row]
                sample_prep = sample_info['Sample Type'][row].upper()
                sample_type = sample_info['Sample Class'][row]
                storage_status = sample_info['Storage Status'][row]
                inventory_status = sample_info['Inventory Status'][row]
                
                
                
                
                sample = etree.SubElement(sample_package, "SAMPLE")
                
                sample_attributes = ["PARENT_NUMBER", "SAMPLE_NUMBER", "EXTERNAL_NUMBER", "RECEIPT_DATE", "COLLECTION_DATE", "INSTITUTION", 
                                     "PREP_DATE", "PREP_BY", "COLLECTED_BY", "STORAGE_ADDRESS", "SAMPLE_TYPE", "SAMPLE_CATEGORY", 
                                     "IS_COMPOSITE", "ARRAY_SIZE_X", "ARRAY_SIZE_Y", "MAPPING_STATUS", "SAMPLE_PREP", "DISEASE_CODE", 
                                     "SITE_CODE", "SITE_OF_TISSUE", "DONOR_AGE", "AGE_UNITS", "SEX", "SPECIES", 
                                     "FT_CYCLES", "QTY_UNITS", "CONC_UNITS", "QTY_ORIGINAL", "QTY_ON_HAND", "CONCENTRATION", 
                                     "STORAGE_STATUS", "PREP_STATUS", "COMMENTS", "INVENTORY_STATUS", "IMAGE_URL", "EXPIRY_DATE"]
                       
                for attribute in sample_attributes:
                    if attribute == "SAMPLE_NUMBER":
                        etree.SubElement(sample, attribute).text = sample_number
                    elif attribute == "STORAGE_ADDRESS":
                        etree.SubElement(sample, attribute).text = storage_address
                    elif attribute == "SAMPLE_TYPE":
                        etree.SubElement(sample, attribute).text = sample_type
                    elif attribute == "SAMPLE_PREP":
                        etree.SubElement(sample, attribute).text = sample_prep
                    elif attribute == "STORAGE_STATUS":
                        etree.SubElement(sample, attribute).text = storage_status
                    elif attribute == "INVENTORY_STATUS":
                        etree.SubElement(sample, attribute).text = inventory_status
                    else:
                        etree.SubElement(sample, attribute, {attr_qname_nil: "true"})
                        
                row += 1
                if row >= num_rows:
                    break
                
            if row >= num_rows:
                break
    
    
    import_tree = etree.ElementTree(import_package)
    
    if folder_type == "same":
        output = os.path.join(file_path[0:-4] + ".xml")

    elif folder_type == "back":
        path, file = os.path.split(file_path)
        path_1, path_2 = os.path.split(path)
        output = os.path.join(path_1, file[0:-4] + ".xml")
        
        if not os.path.exists(os.path.join(path_1, "Please move imported XML files here")):
            os.makedirs(os.path.join(path_1, "Please move imported XML files here"))
    #output = sys.stdout
    
    import_tree.write(output, pretty_print=True)
    

def main():
    file_name = "CDDOM   11-29-2018   14h 13m 52s.csv"
#    file_path = os.path.join(os.pardir, "Collections", "CDDOM", "Import Packages", file_name)
    Generate_XML_File(file_name, "same")
    
if __name__ == '__main__':
    main()