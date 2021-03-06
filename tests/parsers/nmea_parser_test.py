'''
Created on May 27, 2019

@author: jeff
'''
import unittest

from parsers.nmea_parser import NmeaRmcExtractor, NmeaParser
from converter.data_state import DataState

class NmeaParserTest(unittest.TestCase):

    test_state = DataState()
    test_parser = NmeaParser(test_state)

    def test_rmc_1(self):
        test_fields = ["$GPRMC","040338.445","A","3943.8653","N","10456.9499","W","042.7","203.2","190519","","","A*7D"]
        test_extractor = NmeaRmcExtractor()
        test_extractor.extractData(test_fields, NmeaParserTest.test_state)
        self.assertAlmostEqual(self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Latitude)), 39.7310883333, 8)
        self.assertAlmostEqual(self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Longitude)), -104.949165000, 8)
        self.assertAlmostEqual(self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.GPS_KPH)), 79.08040000000001, 8)
        self.assertAlmostEqual(self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.GPS_Heading)), 203.20000000, 8)
        self.assertEqual(self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.GPS_Date)), '2019-05-19')
        self.assertEqual(self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.GPS_Time)), '04:03:38.445')                  
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()