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
            'DateTime',
            'GPS_Time',
            'GPS_Date',
            'Latitude',
            'Longitude',
            'Altitude',
            'X',
            'Y',
            'Z',
            'KPH',
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
            'Accuracy',
            'Sport_Mode',
            'Pasm_Sport_Mode',
            'PSM_Disable',
            'EOL'
    ])

    def __init__(self):
        '''
        Constructor
        '''
        self.state_time = 0.0
        self.state = dict()
        self.state['Lap'] = 0
        self.state['Altitude'] = 0.0
        self.dirty = set()
    
    @staticmethod
    def get_data_names():
        return list(DataState.names)
    
    @staticmethod
    def get_data_name_at_idx(idx):
        return DataState.names[idx]

    def clean(self):
        self.dirty.clear()
        
    def clean_fields(self, field_names):
        for name in field_names:
            if name in self.dirty:
                self.dirty.remove(name)
        
    def get_dirty_fields(self):
        return frozenset(self.dirty)
    
    def is_dirty(self, field_name):
        return field_name in self.dirty
        
    def set_data_item(self, name, value):
        if name not in DataState.names:
            raise ValueError("The name [{0}] is not in the defined set of data names: {1}".format(name, DataState.names))
        if name == 'Time':
            if value != self.state_time:
                self.state_time = value
        self.state[name] = value
        self.dirty.add(name)
        
    def get_data_item(self, name):
        if name not in DataState.names:
            raise ValueError("The name [{0}] is not in the defined set of data names: {1}".format(name, DataState.names))
        return self.state.get(name,"")
    