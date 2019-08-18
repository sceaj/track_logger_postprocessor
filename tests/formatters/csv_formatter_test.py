'''
Created on Jun 20, 2019

@author: Jeffrey
'''
import unittest
from formatters.csv_formatter import CsvFormatter
from converter.data_state import DataState


class CsvFormatterTest(unittest.TestCase):

    def setUp(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
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
        self.test_formatter = CsvFormatter(dict())
        pass

    def testFormatHeader(self):
        test_csv_line = self.test_formatter.formatHeading(self.test_state)
        self.assertEqual("Time, GPS_Time, GPS_Date, Latitude, Longitude, Altitude, X, Y, Z, KPH, Lap, RPM, Gear, Throttle, ECU_Throttle, Brake, Brake_Pressure, Clutch, Steering_Angle, Steering_Rate, Coolant_Temperature, Oil_Pressure, Oil_Temperature, LF_KPH, RF_KPH, LR_KPH, RR_KPH, PSM, GPS_KPH, GPS_Heading, Accuracy, Sport_Mode, Pasm_Sport_Mode, PSM_Disable",
                test_csv_line,
                "The generated CSV line doesn't match the expected value.")
        pass
    
    def testFormatLine(self):
        test_csv_line = self.test_formatter.formatTimeIncrement(self.test_state)
        self.assertEqual("321.36, 21:23:48.021, 15-05-19, 39.7392, 104.9903, 1609, 0.15, 0.86, 1.18, 86.30, 3, 5891, 3, 97, 95, 1, 42, 0, 6.21, 0.42, 99, 240, 96, 85.20, 86.90, 85.00, 86.70, 0, 0.86, 321.41, 0.10, , , ",
                test_csv_line,
                "The generated CSV line doesn't match the expected value.")
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()