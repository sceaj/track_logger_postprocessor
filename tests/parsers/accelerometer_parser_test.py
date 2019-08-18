'''
Created on Jun 21, 2019

@author: Jeffrey
'''
import unittest
from parsers.accelerometer_parser import AccelerometerParser
from converter.data_state import DataState


class Test(unittest.TestCase):

    def setUp(self):
        self.test_state = DataState()
        self.test_parser = AccelerometerParser(self.test_state)

    def testParse(self):
        test_line = "$AC001,477.72,524,598,626"
        self.test_parser.parse(test_line)
        self.assertEqual(477.72, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Time)), 'Time was not parsed correctly.')
        self.assertAlmostEqual(0.23, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.X)), 2, 'X acceleration was not parsed correctly.')
        self.assertAlmostEqual(0.84, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Y)), 2, 'Y acceleration was not parsed correctly.')
        self.assertAlmostEqual(1.03, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Z)), 2, 'Z acceleration was not parsed correctly.')                 
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()