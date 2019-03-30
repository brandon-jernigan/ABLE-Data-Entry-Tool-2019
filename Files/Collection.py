# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 01:20:25 2019

@author: Brandon
"""


class Collection:

    # Initializer / Instance Attributes
    def __init__(self, name, code=""):

        # Current Storage Related Variables
        self.minus_80_2ml_storage = ""
        self.minus_80_4ml_storage = ""
        self.dewar_storage = ""
        self.blood_card_storage = ""

        # Collection Properties
        self.name = name
        self.code = code
        self.donor_dict = {}
        self.import_package_dict = {}


class Import_Package:
    def __init__(self, user_name, collection_name, date="", time=""):

        self.collection = ""
        self.user_name = user_name
        self.collection_name = collection_name
        self.time = time
        self.donor_dict = {}


class Donor:
    """
     [summary]
    
    [description]
    """

    def __init__(self, donor_id, study_id="", mrn=""):

        self.import_package = ""
        self.collection = ""
        self.donor_id = donor_id
        self.study_id = study_id
        self.mrn = mrn
        self.event_dict = {}


class Event:
    def __init__(self, event_name, event_number=""):

        self.donor = ""
        self.import_package = ""
        self.collection = ""
        self.event_name = event_name
        self.event_number = event_number
        self.sample_dict = {}


# TODO: blah blah blah
# ! yikes


class Sample:
    def __init__(self, sample_id):

        self.event = ""
        self.donor = ""
        self.import_package = ""
        self.collection = ""
        self.sample_id = sample_id
        self.storage_location = ""


new_collection = Collection(name="CDDOM")

new_package = Import_Package(user_name="BDJ", collection_name="CDDOM")

new_donor = Donor(donor_id="AT123")

new_event = Event(event_name="001")

new_sample = Sample(sample_id="AT123-001-001")

new_event.sample_dict[new_sample.sample_id] = new_sample
new_donor.event_dict[new_event.event_name] = new_event
new_package.donor_dict[new_donor.donor_id] = new_donor
