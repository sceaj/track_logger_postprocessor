'''
Created on May 21, 2019

@author: jeff
'''

from converter.data_state import DataState
from datetime import datetime
from datetime import timezone
import unittest


class Test(unittest.TestCase):

    object_under_test = DataState()

    def test_get_data_name_at_index(self):
        actual_name = Test.object_under_test.get_data_name_at_idx(DataState.names.RPM)
        self.assertEqual("RPM", actual_name, "The field name for RPM was not looked up correctly.")
        actual_name = Test.object_under_test.get_data_name_at_idx(DataState.names.Oil_Pressure)
        self.assertEqual("Oil_Pressure", actual_name, "The field name for Oil Pressure was not looked up correctly.")
        pass
        
    def test_dirty_marking(self):
        Test.object_under_test.set_data_item('Time', 321.36)
        Test.object_under_test.set_data_item('GPS_Date', '15-05-19')
        Test.object_under_test.set_data_item('GPS_Time', '21:23:48.021')
        Test.object_under_test.set_data_item('X', 0.14)
        Test.object_under_test.set_data_item('Time', 321.41)
        Test.object_under_test.set_data_item('X', 0.10)
        dirty_fields = Test.object_under_test.get_dirty_fields()
        expected_dirty = set({'Time','GPS_Date','GPS_Time','X'})
        self.assertSetEqual(dirty_fields, expected_dirty, 'Expected dirty fields didn''t match the returned actual dirty fields.')

    def test_cleaning_dirty_marking(self):
        Test.object_under_test.set_data_item('Time', 321.36)
        Test.object_under_test.set_data_item('GPS_Date', '15-05-19')
        Test.object_under_test.set_data_item('GPS_Time', '21:23:48.021')
        Test.object_under_test.set_data_item('X', 0.14)
        Test.object_under_test.set_data_item('Time', 321.41)
        Test.object_under_test.set_data_item('X', 0.10)
        dirty_fields = Test.object_under_test.get_dirty_fields()
        self.assertTrue('X' in dirty_fields, 'Expected field X to be dirty.')
        Test.object_under_test.clean_fields(['X', 'GPS_Date', 'GPS_Time'])
        dirty_fields = Test.object_under_test.get_dirty_fields()
        self.assertTrue(Test.object_under_test.is_dirty('Time'), 'Expected field Time to be dirty')
        self.assertFalse(Test.object_under_test.is_dirty('GPS_Date'), 'Expected field GPS_Date to not be dirty')
        self.assertFalse(Test.object_under_test.is_dirty('GPS_Time'), 'Expected field GPS_Time to not be dirty')
        self.assertFalse(Test.object_under_test.is_dirty('X'), 'Expected field X to not be dirty')

    def test_set_data_item(self):
        Test.object_under_test.set_data_item('RPM', 3787)
        self.assertTrue(Test.object_under_test.get_data_item('RPM') == 3787, 'Expected RPM to have value 3787')
        pass
    
    def test_set_data_item_multi(self):
        Test.object_under_test.set_data_item('Time', 321.36)
        Test.object_under_test.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        Test.object_under_test.set_data_item('GPS_Date', '15-05-19')
        Test.object_under_test.set_data_item('GPS_Time', '21:23:48.021')
        Test.object_under_test.set_data_item('X', 0.14)
        Test.object_under_test.set_data_item('Y', 0.86)
        Test.object_under_test.set_data_item('Time', 321.41)
        Test.object_under_test.set_data_item('X', 0.10)
        self.assertTrue(Test.object_under_test.get_data_item('Time') == 321.41, 'Expected Time to have value 321.41')
        self.assertTrue(Test.object_under_test.get_data_item('DateTime') == datetime(2019,5,15,21,23,48,21000,timezone.utc), 'Expected DateTime didn''t match')
        self.assertTrue(Test.object_under_test.get_data_item('GPS_Date') == '15-05-19', 'Expected GPS Date to have value 15-05-19')
        self.assertTrue(Test.object_under_test.get_data_item('GPS_Time') == '21:23:48.021', 'Expected GPS Time to have value 21:23:48.021')
        self.assertTrue(Test.object_under_test.get_data_item('X') == 0.10, 'Expected X accel to have value 0.10')
        self.assertTrue(Test.object_under_test.get_data_item('Y') == 0.86, 'Expected Y accel to have value 0.86')
        pass
    
    def test_get_data_names(self):
        names = Test.object_under_test.get_data_names()
        self.assertTrue('Time' in names)
        self.assertTrue('DateTime' in names)
        self.assertTrue('GPS_Time' in names)
        self.assertTrue('GPS_Date' in names)
        self.assertTrue('Longitude' in names)
        self.assertTrue('Latitude' in names)
        self.assertTrue('Altitude' in names)
        self.assertTrue('X' in names)
        self.assertTrue('Y' in names)
        self.assertTrue('Z' in names)
        self.assertTrue('KPH' in names)
        self.assertTrue('Lap' in names)
        self.assertTrue('RPM' in names)
        self.assertTrue('Gear' in names)
        self.assertTrue('Throttle' in names)
        self.assertTrue('Brake' in names)
        self.assertTrue('Clutch' in names)
        self.assertTrue('Steering_Angle' in names)
        self.assertTrue('Steering_Rate' in names)
        self.assertTrue('Coolant_Temperature' in names)
        self.assertTrue('Oil_Pressure' in names)
        self.assertTrue('Oil_Temperature' in names)
        self.assertTrue('PSM' in names)
        self.assertTrue('GPS_KPH' in names)
        self.assertTrue('GPS_Heading' in names)
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()