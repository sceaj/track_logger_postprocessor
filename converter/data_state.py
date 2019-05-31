'''
Created on May 20, 2019

@author: sceaj
'''

from util.enum import Enum
    
class DataState(object):
    '''
    classdocs
    '''
    
    names = Enum([
            'Time',
            'GPS_Time',
            'GPS_Date',
            'Latitude',
            'Longitude',
            'Altitude',
            'X',
            'Y',
            'Z',
            'KPH',
            'GPS_KPH',
            'Heading',
            'Lap',
            'RPM',
            'Gear',
            'Throttle',
            'ECU_Throttle',
            'Brake',
            'Brake_Pressure',
            'Clutch',
            'Steering_Angle',
            'Steering_Rate',
            'Coolant_Temperature',
            'Oil_Pressure',
            'Oil_Temperature',
            'LF_KPH',
            'RF_KPH',
            'LR_KPH',
            'RR_KPH',
            'PSM',
            'GPS_KPH',
            'GPS_Heading',
            'Accuracy'
    ])

    def __init__(self):
        '''
        Constructor
        '''
        self.state_time = 0.0
        self.state = dict()
    
    @staticmethod
    def get_data_names():
        return list(DataState.names)
    
    @staticmethod
    def get_data_name_at_idx(idx):
        return DataState.names[idx]

    def set_data_item(self, name, value):
        if name not in DataState.names:
            raise ValueError("The name [{0}] is not in the defined set of data names: {1}".format(name, DataState.names))
        self.state[name] = value
        
    def get_data_item(self, name):
        if name not in DataState.names:
            raise ValueError("The name [{0}] is not in the defined set of data names: {1}".format(name, DataState.names))
        return self.state[name]