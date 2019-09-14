'''
Created on Aug 17, 2019

@author: Jeffrey
'''
import unittest
from converter.data_state import DataState
from datetime import datetime
from datetime import timezone
from formatters.influxdb_formatter import InfluxDbFormatter

class InfluxDbFormatterTest(unittest.TestCase):


    def setUp(self):
        self.test_formatter = InfluxDbFormatter(dict(vin='WP0AB29858U782772', vehicle='cayman', mileage='79832', temperature='24'))
        pass

    def testLocation(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('GPS_Time', '21:23:48.021')
        self.test_state.set_data_item('GPS_Date', '15-05-19')
        self.test_state.set_data_item('Latitude', 39.739242)
        self.test_state.set_data_item('Longitude', 104.9903299)
        self.test_state.set_data_item('Altitude', 1609)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'location,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3,geohash=00000000 latitude=39.739242,longitude=104.9903299,altitude=1609 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for locaation was not as expected.')
        self.assertTrue('Latitude' not in self.test_state.get_dirty_fields(), 'Latitude still dirty after formatting.')
        self.assertTrue('Longitude' not in self.test_state.get_dirty_fields(), 'Longitude still dirty after formatting.')
        #self.assertTrue('Altitude' not in self.test_state.get_dirty_fields(), 'Altitude still dirty after formatting.')

    def testAcceleration(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('GPS_Time', '21:23:48.021')
        self.test_state.set_data_item('GPS_Date', '15-05-19')
        self.test_state.set_data_item('X', 0.15)
        self.test_state.set_data_item('Y', 0.86)
        self.test_state.set_data_item('Z', 1.18)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'acceleration,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 x=0.15,y=0.86,z=1.18 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for acceleration was not as expected.')
        self.assertTrue('X' not in self.test_state.get_dirty_fields(), 'X still dirty after formatting.')
        self.assertTrue('Y' not in self.test_state.get_dirty_fields(), 'Y still dirty after formatting.')
        self.assertTrue('Z' not in self.test_state.get_dirty_fields(), 'Z still dirty after formatting.')

    def testSteering(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Steering_Angle', 6.21)
        self.test_state.set_data_item('Steering_Rate', 0.42)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'steering,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 angle=6.21,rate=0.42 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for steering was not as expected.')
        self.assertTrue('Steering_Angle' not in self.test_state.get_dirty_fields(), 'Steering_Angle still dirty after formatting.')
        self.assertTrue('Steering_Rate' not in self.test_state.get_dirty_fields(), 'Steering_Rate still dirty after formatting.')

    def testThrottle(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Throttle', 97)
        self.test_state.set_data_item('ECU_Throttle', 95)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'throttle,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 driver=97,ecu=95 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for throttle was not as expected.')
        self.assertTrue('Throttle' not in self.test_state.get_dirty_fields(), 'Throttle still dirty after formatting.')
        self.assertTrue('ECU_Throttle' not in self.test_state.get_dirty_fields(), 'ECU_Throttle still dirty after formatting.')
        
    def testBrake(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Brake', 1)
        self.test_state.set_data_item('Brake_Pressure', 42)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'brake,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 applied=1,pressure=42 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for brake was not as expected.')
        self.assertTrue('Brake' not in self.test_state.get_dirty_fields(), 'Brake still dirty after formatting.')
        self.assertTrue('Brake_Pressure' not in self.test_state.get_dirty_fields(), 'Brake_Pressure still dirty after formatting.')

    def testClutch(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Clutch', 0)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'clutch,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 released=0 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for clutch was not as expected.')
        self.assertTrue('Clutch' not in self.test_state.get_dirty_fields(), 'Clutch still dirty after formatting.')

    def testRPM(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('RPM', 5996)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'rpm,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 value=5996 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for rpm was not as expected.')
        self.assertTrue('RPM' not in self.test_state.get_dirty_fields(), 'RPM still dirty after formatting.')

    def testCoolantTemperature(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Coolant_Temperature', 99)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'coolant_temperature,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 value=99 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for coolant_temperature was not as expected.')
        self.assertTrue('Coolant_Temperature' not in self.test_state.get_dirty_fields(), 'Coolant_Temperature still dirty after formatting.')

    def testOilPressure(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Oil_Pressure', 240)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'oil_pressure,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 value=240 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for oil_pressure was not as expected.')
        self.assertTrue('Oil_Pressure' not in self.test_state.get_dirty_fields(), 'Oil_Pressure still dirty after formatting.')

    def testOilTemperature(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Oil_Temperature', 96)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'oil_temperature,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 value=96 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for oil_temperature was not as expected.')
        self.assertTrue('Oil_Temperature' not in self.test_state.get_dirty_fields(), 'Oil_Temperature still dirty after formatting.')

    def testWheelSpeed(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('LF_KPH', 85.2)
        self.test_state.set_data_item('RF_KPH', 86.9)
        self.test_state.set_data_item('LR_KPH', 85.0)
        self.test_state.set_data_item('RR_KPH', 86.7)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'wheel_speed,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 left_front=85.2,right_front=86.9,left_rear=85.0,right_rear=86.7 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for wheel_speed was not as expected.')
        self.assertTrue('LF_KPH' not in self.test_state.get_dirty_fields(), 'LF_KPH still dirty after formatting.')
        self.assertTrue('RF_KPH' not in self.test_state.get_dirty_fields(), 'RF_KPH still dirty after formatting.')
        self.assertTrue('LR_KPH' not in self.test_state.get_dirty_fields(), 'LR_KPH still dirty after formatting.')
        self.assertTrue('RR_KPH' not in self.test_state.get_dirty_fields(), 'RR_KPH still dirty after formatting.')

    def testPModes(self):
        self.test_state = DataState()
        self.test_state.set_data_item('Time', 321.36)
        self.test_state.set_data_item('DateTime', datetime(2019,5,15,21,23,48,21000,timezone.utc))
        self.test_state.set_data_item('Sport_Mode', 1)
        self.test_state.set_data_item('Pasm_Sport_Mode', 1)
        self.test_state.set_data_item('PSM_Disable', 0)
        self.test_state.set_data_item('Lap', 3)
        actual = self.test_formatter.formatData(self.test_state)
        expected = 'pmodes,vehicle=cayman,vin=WP0AB29858U782772,mileage=79832,lap=3 sport=1,pasm_sport=1,psm_off=0 1557955428021'
        self.assertEqual(expected, actual[0], 'The generated influxdb line protocol data for pmodes was not as expected.')
        self.assertTrue('Sport_Mode' not in self.test_state.get_dirty_fields(), 'Sport_Mode still dirty after formatting.')
        self.assertTrue('Pasm_Sport_Mode' not in self.test_state.get_dirty_fields(), 'Pasm_Sport_Mode still dirty after formatting.')
        self.assertTrue('PSM_Disable' not in self.test_state.get_dirty_fields(), 'PSM_Disable still dirty after formatting.')

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()