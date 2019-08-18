'''
Created on May 20, 2019

@author: sceaj
'''
from converter.data_state import DataState
from util.enum import Enum

class CanFrame0C2Extractor(object):
    
    def extractData(self, field_data, state):
        steering_angle = CanFrameParser.frame_int16(field_data, 0)
        steering_angle_sign = steering_angle & 0x8000
        steering_angle &= 0xEFFF
        if (steering_angle_sign == 0):
            steering_angle *= -1
        state.set_data_item(DataState.names[DataState.names.Steering_Angle], int(steering_angle))
        steering_rate = CanFrameParser.frame_int16(field_data, 2)
        steering_rate_sign = steering_rate & 0x8000
        steering_rate &= 0xEFFF
        if (steering_rate_sign == 0):
            steering_rate *= -1
        state.set_data_item(DataState.names[DataState.names.Steering_Rate], int(steering_rate))
        print("Steering_Angle: {0}".format(steering_angle))
        print("Steering_Rate: {0}".format(steering_rate))
                
class CanFrame14AExtractor(object):
    
    def extractData(self, field_data, state):
        psm_disable = 1 if (CanFrameParser.frame_byte(field_data, 1) & 0x20) == 0x20 else 0
        state.set_data_item(DataState.names[DataState.names.PSM_Disable], psm_disable)
        print("PSM_Disable: {0}".format(psm_disable))
 
class CanFrame242Extractor(object):
    
    def extractData(self, field_data, state):
        clutch_pedal = 1 if (CanFrameParser.frame_byte(field_data, 0) & 0x08) == 0x08 else 0
        state.set_data_item(DataState.names[DataState.names.Clutch], clutch_pedal)
        engine_rpm = int(CanFrameParser.frame_word(field_data, 2) / 4)
        state.set_data_item(DataState.names[DataState.names.RPM], engine_rpm)
        ecu_throttle = int(CanFrameParser.frame_byte(field_data, 5) * 100 / 255)
        state.set_data_item(DataState.names[DataState.names.ECU_Throttle], ecu_throttle)
        print("Clutch: {0}".format(clutch_pedal))
        print("RPM: {0}".format(engine_rpm))
        print("ECU_Throttle: {0}".format(ecu_throttle))

class CanFrame245Extractor(object):
    
    def extractData(self, field_data, state):
        coolant_temp = (CanFrameParser.frame_byte(field_data, 1) * 4 / 3) - 48
        state.set_data_item(DataState.names[DataState.names.Coolant_Temperature], coolant_temp)
        brake_pedal = 1 if (CanFrameParser.frame_byte(field_data, 2) & 0x02) == 0x02 else 0
        state.set_data_item(DataState.names[DataState.names.Brake], brake_pedal)
        print("Coolant: {0}".format(coolant_temp))
        print("Brake: {0}".format(brake_pedal))
    
class CanFrame246Extractor(object):
    
    def extractData(self, field_data, state):
        gear_selection = CanFrameParser.frame_byte(field_data, 0) & 0x07
        state.set_data_item(DataState.names[DataState.names.Gear], gear_selection)
        throttle_pedal = int(CanFrameParser.frame_byte(field_data, 3) * 100 / 255)
        state.set_data_item(DataState.names[DataState.names.Throttle], throttle_pedal)
        print("Gear: {0}".format(gear_selection))
        print("Throttle: {0}".format(throttle_pedal))

class CanFrame24AExtractor(object):
    
    def extractData(self, field_data, state):
        lf_wheel_speed = CanFrameParser.frame_word(field_data, 0) / 100
        state.set_data_item(DataState.names[DataState.names.LF_KPH], lf_wheel_speed)
        rf_wheel_speed = CanFrameParser.frame_word(field_data, 2) / 100
        state.set_data_item(DataState.names[DataState.names.RF_KPH], rf_wheel_speed)
        lr_wheel_speed = CanFrameParser.frame_word(field_data, 4) / 100
        state.set_data_item(DataState.names[DataState.names.LR_KPH], lr_wheel_speed)
        rr_wheel_speed = CanFrameParser.frame_word(field_data, 6) / 100
        state.set_data_item(DataState.names[DataState.names.RR_KPH], rr_wheel_speed)
        print("Left Front KPH: {0}".format(lf_wheel_speed))
        print("Right Front KPH: {0}".format(rf_wheel_speed))
        print("Left Rear KPH: {0}".format(lr_wheel_speed))
        print("Right Rear KPH: {0}".format(rr_wheel_speed))

class CanFrame308Extractor(object):
    
    def extractData(self, field_data, state):
        sport_mode = 1 if (CanFrameParser.frame_byte(field_data, 0) & 0x20) else 0
        state.set_data_item(DataState.names[DataState.names.Sport_Mode], sport_mode)
        print("Sport Mode: {0}".format(sport_mode))

class CanFrame441Extractor(object):
    
    def extractData(self, field_data, state):
        oil_temperature = (CanFrameParser.frame_byte(field_data, 5) * 4 / 3) - 48
        state.set_data_item(DataState.names[DataState.names.Oil_Temperature], oil_temperature)
        oil_pressure = CanFrameParser.frame_byte(field_data, 6) * 25 / 10
        state.set_data_item(DataState.names[DataState.names.Oil_Pressure], oil_pressure)
        print("Oil Temperature: {0}".format(oil_temperature))
        print("Oil Pressure: {0}".format(oil_pressure))

class CanFrame442Extractor(object):
    
    def extractData(self, field_data, state):
        pasm_sport_mode = 1 if (CanFrameParser.frame_byte(field_data, 0) & 0x11) == 0x11 else 0
        state.set_data_item(DataState.names[DataState.names.Pasm_Sport_Mode], pasm_sport_mode)
        print("PASM Sport Mode: {0}".format(pasm_sport_mode))

class CanFrame44BExtractor(object):
    
    def extractData(self, field_data, state):
        brake_pressure = CanFrameParser.frame_byte(field_data, 0)
        state.set_data_item(DataState.names[DataState.names.Brake_Pressure], brake_pressure)
        print("Brake Pressure: {0}".format(brake_pressure))

class CanFrameParser(object):
    '''
    classdocs
    '''
    Fields = Enum(['Mnemonic', 'Time', 'CanId', 'Byte0', 'Byte1', 'Byte2', 'Byte3', 'Byte4', 'Byte5', 'Byte6', 'Byte7'])

    frame_0C2_extractor = CanFrame0C2Extractor()
    frame_14A_extractor = CanFrame14AExtractor()
    frame_242_extractor = CanFrame242Extractor()
    frame_245_extractor = CanFrame245Extractor()
    frame_246_extractor = CanFrame246Extractor()
    frame_24A_extractor = CanFrame24AExtractor()
    frame_308_extractor = CanFrame308Extractor()
    frame_441_extractor = CanFrame441Extractor()
    frame_442_extractor = CanFrame442Extractor()    
    frame_44B_extractor = CanFrame44BExtractor()

    @staticmethod
    def can_time(field_data):
        return float(field_data[CanFrameParser.Fields.Time])
    
    @staticmethod
    def can_id(field_data):
        return int(field_data[CanFrameParser.Fields.CanId], 16)

    @staticmethod
    def extractor_factory(can_id):
        if can_id == 0x0C2:
            return CanFrameParser.frame_0C2_extractor
        elif can_id == 0x14A:
            return CanFrameParser.frame_14A_extractor
        elif can_id == 0x242:
            return CanFrameParser.frame_242_extractor
        elif can_id == 0x245:
            return CanFrameParser.frame_245_extractor
        elif can_id == 0x246:
            return CanFrameParser.frame_246_extractor
        elif can_id == 0x24A:
            return CanFrameParser.frame_24A_extractor
        elif can_id == 0x308:
            return CanFrameParser.frame_308_extractor
        elif can_id == 0x441:
            return CanFrameParser.frame_441_extractor
        elif can_id == 0x442:
            return CanFrameParser.frame_442_extractor
        elif can_id == 0x44B:
            return CanFrameParser.frame_44B_extractor
        else:
            raise ValueError("No known extractor for CAN ID 0x{0:X}".format(can_id))
            
    @staticmethod
    def frame_byte(field_data, byte_idx):
        if byte_idx == 0:
            return int(field_data[CanFrameParser.Fields.Byte0], 16)
        elif byte_idx == 1:
            return int(field_data[CanFrameParser.Fields.Byte1], 16)
        elif byte_idx == 2:
            return int(field_data[CanFrameParser.Fields.Byte2], 16)
        elif byte_idx == 3:
            return int(field_data[CanFrameParser.Fields.Byte3], 16)
        elif byte_idx == 4:
            return int(field_data[CanFrameParser.Fields.Byte4], 16)
        elif byte_idx == 5:
            return int(field_data[CanFrameParser.Fields.Byte5], 16)
        elif byte_idx == 6:
            return int(field_data[CanFrameParser.Fields.Byte6], 16)
        elif byte_idx == 7:
            return int(field_data[CanFrameParser.Fields.Byte7], 16)
        else:
            raise ValueError("The byte index of a CAN frame must be between 0 and 7")

    @staticmethod
    def frame_word(field_data, word_idx):
        if word_idx == 0:
            return int(field_data[CanFrameParser.Fields.Byte1] + field_data[CanFrameParser.Fields.Byte0], 16)
        elif word_idx == 2:
            return int(field_data[CanFrameParser.Fields.Byte3] + field_data[CanFrameParser.Fields.Byte2], 16)
        elif word_idx == 4:
            return int(field_data[CanFrameParser.Fields.Byte5] + field_data[CanFrameParser.Fields.Byte4], 16)
        elif word_idx == 6:
            return int(field_data[CanFrameParser.Fields.Byte7] + field_data[CanFrameParser.Fields.Byte7], 16)
        else:
            raise ValueError("The word index of a CAN frame must be 0, 2, 4, or 6")
        
    @staticmethod
    def frame_int16(field_data, word_idx):
        value = CanFrameParser.frame_word(field_data, word_idx)
        if (value > 32767):
            value -= 65535
        return value

    def __init__(self, state):
        '''
        Constructor
        '''
        self.state = state
        
    def parse(self, sentence):
        field_data = sentence.split(',')
        try:
            extractor = CanFrameParser.extractor_factory(CanFrameParser.can_id(field_data))
            extractor.extractData(field_data, self.state)
            self.state.set_data_item(DataState.names[DataState.names.Time], CanFrameParser.can_time(field_data))
        except (ValueError, IndexError) as err:
            print("Failed to parse CAN message: {0}".format(err))
            
        
