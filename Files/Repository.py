# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 01:20:25 2019

@author: Brandon
"""

class Repository:

    def __init__(self):

        self.device_dict = {}

class Device:

    def __init__(self, address, name, type):

        self.name = ''
        self.top_device = ''
        self.held_by = ''
        self.address = ''
        self.type = ''  # Dewar, -80 Freezer, -20 Freezer, Refrigerator
        self.holds = {} # Device or Slots

class Slot:

    def __init__(self, name, held_by, address, collection_assignment, sample_assignment):
        self.name = ''
        self.held_by = ''
        self.address = ''
        self.collection_assignment = ''
        self.sample_assigned = ''


