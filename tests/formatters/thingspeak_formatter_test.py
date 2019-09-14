'''
Created on Aug 18, 2019

@author: sceaj
'''

from converter.data_state import DataState
from datetime import datetime
from datetime import timezone
from formatters.thingspeak_formatter import ThingSpeakFormatter
import json
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('GPS_Time', '21:23:48.021')
        self.test_state.set_data_item('GPS_Date', '15-05-19')
        self.test_state.set_data_item('Latitude', 39.739242)
        self.test_state.set_data_item('Longitude', 104.9903299)
        self.test_state.set_data_item('Altitude', 1609)
        self.test_state.set_data_item('X', 0.15)
        self.test_state.set_data_item('Y', 0.86)
        self.test_state.set_data_item('Z', 1.18)
        self.test_state.set_data_item('KPH', 86.3)
        self.test_state.set_data_item('Lap', 3)
        self.test_state.set_data_item('RPM', 5891)
        self.test_state.set_data_item('Gear', 3)
        self.test_state.set_data_item('Throttle', 97)
        self.test_state.set_data_item('ECU_Throttle', 95)
        self.test_state.set_data_item('Brake', 1)
        self.test_state.set_data_item('Brake_Pressure', 42)
        self.test_state.set_data_item('Clutch', 0)
        self.test_state.set_data_item('Steering_Angle', 6.21)
        self.test_state.set_data_item('Steering_Rate', 0.42)
        self.test_state.set_data_item('Coolant_Temperature', 99)
        self.test_state.set_data_item('Oil_Pressure', 240)
        self.test_state.set_data_item('Oil_Temperature', 96)
        self.test_state.set_data_item('LF_KPH', 85.2)
        self.test_state.set_data_item('RF_KPH', 86.9)
        self.test_state.set_data_item('LR_KPH', 85.0)
        self.test_state.set_data_item('RR_KPH', 86.7)
        self.test_state.set_data_item('PSM', 0)
        self.test_state.set_data_item('GPS_KPH', 0.86)
        self.test_state.set_data_item('GPS_Heading', 321.41)
        self.test_state.set_data_item('Accuracy', 0.10)
        self.test_formatter = ThingSpeakFormatter(dict())
        pass

    def testFormatDate(self):
        actual_json = self.test_formatter.formatTimeIncrement(self.test_state)
        print(actual_json)
        actual = json.loads(actual_json)
        self.assertAlmostEqual(39.739242, actual['Latitude'], 6)
        self.assertAlmostEqual(104.9903299, actual['Longitude'], 6)
        self.assertAlmostEqual(1609, actual['Elevation'], 3)
        self.assertAlmostEqual(0.15, actual['Field1'], 3)
        self.assertAlmostEqual(0.86, actual['Field2'], 3)
        self.assertAlmostEqual(1.18, actual['Field3'], 3)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()