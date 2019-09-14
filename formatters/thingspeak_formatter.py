'''
Created on Aug 18, 2019

@author: sceaj
'''

from converter.data_state import DataState
import datetime
import json

class ThingSpeakFormatter(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

    def formatHeading(self, data_state):
        return None
    
    def formatData(self, data_state):
        return None
        
    def formatTimeIncrement(self, data_state):
        speak_thing = dict()
        speak_thing['Timestamp'] = data_state.get_data_item('DateTime').isoformat()
        speak_thing['Latitude'] = data_state.get_data_item('Latitude')
        speak_thing['Longitude'] = data_state.get_data_item('Longitude')
        speak_thing['Elevation'] = data_state.get_data_item('Altitude')
        speak_thing['field1'] = data_state.get_data_item('X')
        speak_thing['field2'] = data_state.get_data_item('Y')
        speak_thing['field3'] = data_state.get_data_item('Z')
        speak_thing['field4'] = data_state.get_data_item('KPH')
        speak_thing['field5'] = data_state.get_data_item('Lap')
        speak_thing['field6'] = data_state.get_data_item('RPM')
        speak_thing['field7'] = data_state.get_data_item('Gear')
        speak_thing['field8'] = data_state.get_data_item('Throttle')
        speak_thing['field9'] = data_state.get_data_item('ECU_Throttle')
        speak_thing['field10'] = data_state.get_data_item('Brake')
        speak_thing['field11'] = data_state.get_data_item('Brake_Pressure')
        speak_thing['field12'] = data_state.get_data_item('Clutch')
        speak_thing['field13'] = data_state.get_data_item('Steering_Angle')
        speak_thing['field14'] = data_state.get_data_item('Steering_Rate')
        speak_thing['field15'] = data_state.get_data_item('Coolant_Temperature')
        speak_thing['field16'] = data_state.get_data_item('Oil_Pressure')
        speak_thing['field17'] = data_state.get_data_item('Oil_Temperature')
        speak_thing['field18'] = data_state.get_data_item('LF_KPH')
        speak_thing['field19'] = data_state.get_data_item('RF_KPH')
        speak_thing['field20'] = data_state.get_data_item('LR_KPH')
        speak_thing['field21'] = data_state.get_data_item('RR_KPH')
        speak_thing['field22'] = data_state.get_data_item('PSM')
        speak_thing['field23'] = data_state.get_data_item('GPS_KPH')
        speak_thing['Field24'] = data_state.get_data_item('GPS_Heading')
        speak_thing['Field25'] = data_state.get_data_item('Accuracy')
        speak_thing['Field26'] = data_state.get_data_item('Sport_Mode')
        speak_thing['Field27'] = data_state.get_data_item('Pasm_Sport_Mode')
        speak_thing['Field28'] = data_state.get_data_item('PSM_Disable')
        return json.dumps(speak_thing)        
        
    def formatFooter(self, data_state):
        return None