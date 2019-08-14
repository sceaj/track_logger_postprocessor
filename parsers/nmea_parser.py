'''
Created on May 20, 2019

@author: sceaj
'''
from converter.data_state import DataState
from util.enum import Enum

class NmeaRmcExtractor(object):

    Fields = Enum(['Mnemonic', 'GPS_Time', 'GPS_Status', 'Latitude', 'Latitude_Direction', 'Longitude', 'Longitude_Direction', 'Speed', 'Track', 'GPS_Date', 'Magnetic_Variation', "Checksum"])

    def extractData(self, field_data, state):
        gps_state = field_data[NmeaRmcExtractor.Fields.GPS_Status]
        if (gps_state == 'A'):
            gps_raw_time = field_data[NmeaRmcExtractor.Fields.GPS_Time]
            gps_time = "{0}:{1}:{2}".format(gps_raw_time[0:2], gps_raw_time[2:4], gps_raw_time[4:])
            state.set_data_item(DataState.names[DataState.names.GPS_Time], gps_time)
            gps_raw_date = field_data[NmeaRmcExtractor.Fields.GPS_Date]
            gps_date = "20{2}-{1}-{0}".format(gps_raw_date[0:2], gps_raw_date[2:4], gps_raw_date[4:6])
            state.set_data_item(DataState.names[DataState.names.GPS_Date], gps_date)
            gps_raw_lat = field_data[NmeaRmcExtractor.Fields.Latitude]
            latitude = NmeaParser.convert_degrees(gps_raw_lat)
            if (field_data[NmeaRmcExtractor.Fields.Latitude_Direction] == 'S'):
                latitude = latitude * -1.0
            state.set_data_item(DataState.names[DataState.names.Latitude], latitude)
            gps_raw_long = field_data[NmeaRmcExtractor.Fields.Longitude]
            longitude = NmeaParser.convert_degrees(gps_raw_long)
            if (field_data[NmeaRmcExtractor.Fields.Longitude_Direction] == 'W'):
                longitude = longitude * -1.0
            state.set_data_item(DataState.names[DataState.names.Longitude], longitude)
            gps_kph = float(field_data[NmeaRmcExtractor.Fields.Speed]) * 1.852
            state.set_data_item(DataState.names[DataState.names.GPS_KPH], gps_kph)
            gps_heading = float(field_data[NmeaRmcExtractor.Fields.Track])
            state.set_data_item(DataState.names[DataState.names.GPS_Heading], gps_heading)


class NmeaParser(object):
    '''
    classdocs
    '''
    
    rmc_extractor = NmeaRmcExtractor()
    
    @staticmethod
    def extractor_factory(mnemonic):
        if mnemonic == '$GPRMC':
            return NmeaParser.rmc_extractor
        else:
            return None
        
    @staticmethod
    def convert_degrees(raw_value):
        minutes_index = raw_value.find(".")
        degress = float(raw_value[0:minutes_index])
        minutes = float(raw_value[minutes_index:]) / 60.0
        return degress + minutes

    def __init__(self, state):
        '''
        Constructor
        '''
        self.state = state
        
    def parse(self, sentence):
        field_data = sentence.split(',')
        extractor = NmeaParser.extractor_factory(field_data[0])
        if extractor is not None:
            extractor.extractData(field_data, self.state)
        else:
            print("No extractor has been written for {0}. Skipping...".format(field_data[0]))

        