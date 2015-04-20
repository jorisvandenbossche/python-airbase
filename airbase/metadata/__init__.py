# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:12:16 2015

@author: Joris Van den Bossche
"""

import zipfile

import pandas as pd


archive_stations = zipfile.ZipFile('airbase/metadata/data/AirBase_v8_stations.zip', 'r')
STATIONS = pd.read_csv(archive_stations.open('AirBase_v8_stations.csv'), sep='\t')

archive_measconfig = zipfile.ZipFile('airbase/metadata/data/AirBase_v8_measurement_configurations.zip', 'r')
MEASUREMENT_CONFIGURATIONS = pd.read_csv(archive_measconfig.open('AirBase_v8_measurement_configurations.csv'), sep='\t')
