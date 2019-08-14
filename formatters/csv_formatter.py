'''
Created on Jun 20, 2019

@author: Jeffrey
'''
from converter.data_state import DataState

class CsvFormatter(object):
    '''
    classdocs
    '''

    def __init__(self, tags):
        '''
        Constructor
        '''
        
    def formatHeading(self, data_state):
        print("Formatting header...")
        csv_line = DataState.names[DataState.names.Time]
        for idx in range(DataState.names.GPS_Time, DataState.names.EOL):
            csv_line += ", "
            csv_line += DataState.get_data_name_at_idx(idx)
        return csv_line
        
    def formatTimeIncrement(self, data_state):
        csv_line = "{:.2f}".format(data_state.get_data_item(DataState.names[DataState.names.Time]))
        for idx in range(DataState.names.GPS_Time, DataState.names.EOL):
            csv_line += ", "
            column = DataState.get_data_name_at_idx(idx)
            value = data_state.get_data_item(column)
            if isinstance(value, str):
                csv_line += value
            elif idx == DataState.names.Latitude or idx == DataState.names.Longitude:
                csv_line += "{:.4f}".format(value)
##            elif idx == DataState.names.Throttle or idx == DataState.names.ECU_Throttle:
##                csv_line += "{:.1f}".format(value)
            elif isinstance(value, float):
                csv_line += "{:.2f}".format(value)
            else:
                csv_line += str(value)
        return csv_line
        
        
    def formatFooter(self, data_state):
        print("Formatting footer...")