'''
Created on May 20, 2019

@author: sceaj
'''
from converter.data_state import DataState
from util.enum import Enum

class AccelerometerParser(object):
    '''
    classdocs
    '''
    Fields = Enum(['Mnemonic', 'Time', 'LongitudinalGs', 'LateralGs', 'VerticalGs'])

    x_zero = 501
    y_zero = 514
    z_zero = 523
    
    scale = 100.0
    
    def __init__(self, state):
        '''
        Constructor
        '''
        self.state = state

    @staticmethod
    def accel_time(field_data):
        return float(field_data[AccelerometerParser.Fields.Time])

    @staticmethod
    def get_raw_value(field_data, idx):
        return int(field_data[idx])
    
    @staticmethod
    def get_adjusted_value(raw_value, zero_value):
        return float(raw_value - zero_value) / AccelerometerParser.scale
            
    def parse(self, sentence):
        field_data = sentence.split(',')
        x_raw = AccelerometerParser.get_raw_value(field_data, AccelerometerParser.Fields.LongitudinalGs)
        x_accel = AccelerometerParser.get_adjusted_value(x_raw, AccelerometerParser.x_zero)
        y_raw = AccelerometerParser.get_raw_value(field_data, AccelerometerParser.Fields.LateralGs)
        y_accel = AccelerometerParser.get_adjusted_value(y_raw, AccelerometerParser.y_zero)
        z_raw = AccelerometerParser.get_raw_value(field_data, AccelerometerParser.Fields.VerticalGs)
        z_accel = AccelerometerParser.get_adjusted_value(z_raw, AccelerometerParser.z_zero)
        self.state.set_data_item(DataState.names[DataState.names.X], x_accel)
        self.state.set_data_item(DataState.names[DataState.names.Y], y_accel)
        self.state.set_data_item(DataState.names[DataState.names.Z], z_accel)
        self.state.set_data_item(DataState.names[DataState.names.Time], AccelerometerParser.accel_time(field_data))
