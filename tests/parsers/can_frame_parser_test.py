'''
Created on May 24, 2019

@author: jeff
'''
import unittest
from parsers.can_frame_parser import CanFrame0C2Extractor
from parsers.can_frame_parser import CanFrame242Extractor, CanFrame245Extractor, CanFrame246Extractor, CanFrame24AExtractor
from parsers.can_frame_parser import CanFrame441Extractor, CanFrame44BExtractor, CanFrameParser
from converter.data_state import DataState



class CanFrameParserTest(unittest.TestCase):

    test_state = DataState()
    test_parser = CanFrameParser(test_state)
        
    def testFrame0C2_1(self):
        CanFrameParser.verbose = True
        test_fields = ["$CNDRV","476.72","0C2","CB","10","15","06","00","00","00","00"]
        test_extractor = CanFrame0C2Extractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertEqual(4299, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Steering_Angle)), 'Steering Angle was not parsed correctly.')
        self.assertEqual(1557, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Steering_Rate)), 'Steering Rate was not parsed correctly.')
        
    def testFrame0C2_2(self):
        CanFrameParser.verbose = True
        test_fields = ["$CNDRV","476.72","0C2","C8","90","15","86","00","00","00","00"]
        test_extractor = CanFrame0C2Extractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertEqual(-4296, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Steering_Angle)), 'Steering Angle was not parsed correctly.')
        self.assertEqual(-1557, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Steering_Rate)), 'Steering Rate was not parsed correctly.')
        
            
    def testFrame242_1(self):
        test_fields = ["$CNDRV","476.72","242","01","00","00","00","58","00","65","00"]
        test_extractor = CanFrame242Extractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertEqual(0, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Clutch)), 'Clutch Pedal was not parsed correctly.')
        self.assertEqual(0, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.RPM)), 'Engine RPM was not parsed correctly.')
        self.assertEqual(0, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.ECU_Throttle)), 'ECU commanded throttle was not parsed correctly.')                 
        pass

    def testFrame242_2(self):
        test_fields = ["$CNDRV","476.72","242","09","00","C8","50","58","C3","65","00"]
        test_extractor = CanFrame242Extractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertEqual(1, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Clutch)), 'Clutch Pedal was not parsed correctly.')
        self.assertEqual(5170, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.RPM)), 'Engine RPM was not parsed correctly.')
        self.assertAlmostEqual(76, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.ECU_Throttle)), 2, 'ECU commanded throttle was not parsed correctly.')                 
        pass

    def testFrame245(self):
        test_fields = ["$CNDRV","476.72","245","01","6C","02","00","58","00","65","00"]
        test_extractor = CanFrame245Extractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertEqual(96, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Coolant_Temperature)), 'Coolant temperature was not parsed correctly.')
        self.assertEqual(1, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Brake)), 'Brake pedal was not parsed correctly.')
        pass

    def testFrame246(self):
        test_fields = ["$CNDRV","476.72","246","0B","00","C8","E1","58","C3","65","00"]
        test_extractor = CanFrame246Extractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertEqual(3, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Gear)), 'Gear indicator was not parsed correctly.')
        self.assertAlmostEqual(88, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Throttle)), 2, 'ECU commanded throttle was not parsed correctly.')                 
        pass

    def testFrame24A(self):
        test_fields = ["$CNDRV","476.72","24A","0B","10","C8","10","0E","10","D2","10"]
        test_extractor = CanFrame24AExtractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertAlmostEqual(41.07, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.LF_KPH)), 2, 'LF wheel speed was not parsed correctly.')
        self.assertAlmostEqual(42.96, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.RF_KPH)), 2, 'RF wheel speed was not parsed correctly.')                 
        self.assertAlmostEqual(41.10, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.LR_KPH)), 2, 'LR wheel speed was not parsed correctly.')
        self.assertAlmostEqual(41.12, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.RR_KPH)), 2, 'RR wheel speed was not parsed correctly.')                 
        pass
    
    def testFrame441(self):
        test_fields = ["$CNDRV","476.72","441","0B","10","C8","10","0E","67","82","10"]
        test_extractor = CanFrame441Extractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertAlmostEqual(89.33, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Oil_Temperature)), 2, 'Oil temperature was not parsed correctly.')
        self.assertEqual(325, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Oil_Pressure)), 'Oil pressure was not parsed correctly.')                 
        pass

    def testFrame44B(self):
        test_fields = ["$CNDRV","476.72","44B","2B","10","C8","10","0E","10","D2","10"]
        test_extractor = CanFrame44BExtractor()
        test_extractor.extractData(test_fields, CanFrameParserTest.test_state)
        self.assertEqual(43, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Brake_Pressure)), 'Brake pressure was not parsed correctly.')                 
        pass
    
    def testParserFrame242(self):
        test_line = "$CNDRV,477.72,242,09,00,C8,50,58,C3,65,00"
        CanFrameParserTest.test_parser.parse(test_line)
        self.assertEqual(477.72, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Time)), 'Time was not parsed correctly.')
        self.assertEqual(1, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Clutch)), 'Clutch Pedal was not parsed correctly.')
        self.assertEqual(5170, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.RPM)), 'Engine RPM was not parsed correctly.')
        self.assertAlmostEqual(76, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.ECU_Throttle)), 2, 'ECU commanded throttle was not parsed correctly.')                 
        pass

    def testParserFrame245(self):
        test_line = "$CNDRV,477.72,245,09,6E,C8,50,58,C3,65,00"
        CanFrameParserTest.test_parser.parse(test_line)
        self.assertAlmostEqual(477.72, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Time)), 2, 'Time was not parsed correctly.')
        self.assertAlmostEqual(98.67, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Coolant_Temperature)), 2, 'Coolant temperature was not parsed correctly.')
        self.assertEqual(0, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Brake)), 'Brake pedal was not parsed correctly.')
        pass

    def testParserFrame246(self):
        test_line = "$CNDRV,478.50,246,04,00,C8,FA,58,C3,65,00"
        CanFrameParserTest.test_parser.parse(test_line)
        self.assertEqual(478.50, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Time)), 'Time was not parsed correctly.')
        self.assertEqual(4, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Gear)), 'Gear indicator was not parsed correctly.')
        self.assertAlmostEqual(98, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Throttle)), 2, 'ECU commanded throttle was not parsed correctly.')                 
        pass
    
    def testParserFrame24A(self):
        test_line = "$CNDRV,480.17,24A,0B,20,C8,20,F7,20,02,21"
        CanFrameParserTest.test_parser.parse(test_line)
        self.assertEqual(480.17, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.Time)), 'Time was not parsed correctly.')
        self.assertAlmostEqual(82.030, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.LF_KPH)), 3, 'LF wheel speed was not parsed correctly.')
        self.assertAlmostEqual(83.920, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.RF_KPH)), 3, 'RF wheel speed was not parsed correctly.')                 
        self.assertAlmostEqual(84.390, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.LR_KPH)), 3, 'LR wheel speed was not parsed correctly.')
        self.assertAlmostEqual(84.810, self.test_state.get_data_item(DataState.get_data_name_at_idx(DataState.names.RR_KPH)), 3, 'RR wheel speed was not parsed correctly.')                 
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testFrame242']
    unittest.main()