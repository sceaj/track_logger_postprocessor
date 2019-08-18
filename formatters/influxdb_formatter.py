'''
Created on Aug 1, 2019

@author: Jeffrey

Influx line protocol
<measurement>[,<tag-key>=<tag-value>...] <field-key>=<field-value>[,<field2-key>=<field2-value>...] [unix-nano-timestamp]

location,vin=<vin>,lap=<lap>,geohash=<geohash> latitude=<999.999999>,longitude=<999.99999>,altitude=<9999>  <timestamp>
acceleration,vin=<vin>,lap=<lap> x=<xg>,y=<yg>,z=<zg> <timestamp>
steering,vin=<vin>,lap=<lap> angle=<99999>,rate=<99999> <timestamp>
throttle,vin=<vin>,lap=<lap> driver=<999>,ecu=<999> <timestamp>
brake,vin=<vin>,lap=<lap> applied=[0/1],pressure=<999> <timestamp>
clutch,vin=<vin>,lap=<lap> released=[0/1] <timestamp>
rpm,vin=<vin>,lap=<lap> value=<9999> <timestamp>
coolant_temperature,vin=<vin>,lap=<lap> value=<coolant-temperature> <timestamp>
oil_pressure,vin=<vin>,lap=<lap> value=<oil-pressure> <timestamp>
oil_temperature,vin=<vin>,lap=<lap> value=<oil-temperature> <timestamp>
wheel_speed,vin=<vin>,lap=<lap> left_front=<lf-kph>,right_front=<rf-kph>,left_rear=<lr-kph>,right_rear=<rr-kph> <timestamp>
pmodes,vin=<vin>,lap=<lap> sport=[0/1],pasm_sport=[0/1],psm_off=[0/1] <timestamp>

'''

from converter.data_state import DataState
from converter.time_util import TimeUtils

class InfluxDbFormatter(object):
    '''
    classdocs
    '''



    def __init__(self, tags):
        '''
        Constructor
        '''
        self.tags = "vehicle={0},vin={1},mileage={2}".format(tags['vehicle'],tags['vin'],tags['mileage'])
        
    def formatHeading(self, data_state):
        return None
        
    def formatData(self, data_state):
        fields = data_state.get_dirty_fields()
        influx_timestamp = TimeUtils.influxDBTimestamp(data_state.get_data_item(DataState.names[DataState.names.DateTime]))
        influx_data_lines = []
        if fields.issuperset(['Latitude', 'Longitude']):
            influx_data_lines.append(self.buildLocation(data_state) + str(influx_timestamp))
        if fields.issuperset(['X', 'Y', 'Z']):
            influx_data_lines.append(self.buildAcceleration(data_state) + str(influx_timestamp))
        if fields.issuperset(['Steering_Angle', 'Steering_Rate']):
            influx_data_lines.append(self.buildSteering(data_state) + str(influx_timestamp))
        if fields.issuperset(['Throttle', 'ECU_Throttle']):
            influx_data_lines.append(self.buildThrottle(data_state) + str(influx_timestamp))
        if fields.issuperset(['Brake', 'Brake_Pressure']):
            influx_data_lines.append(self.buildBrake(data_state) + str(influx_timestamp))
        if fields.issuperset(['Clutch']):
            influx_data_lines.append(self.buildClutch(data_state) + str(influx_timestamp))
        if fields.issuperset(['RPM']):
            influx_data_lines.append(self.buildRPM(data_state) + str(influx_timestamp))
        if fields.issuperset(['Coolant_Temperature']):
            influx_data_lines.append(self.buildCoolant(data_state) + str(influx_timestamp))
        if fields.issuperset(['Oil_Pressure']):
            influx_data_lines.append(self.buildOilPressure(data_state) + str(influx_timestamp))
        if fields.issuperset(['Oil_Temperature']):
            influx_data_lines.append(self.buildOilTemperature(data_state) + str(influx_timestamp))
        if fields.issuperset(['LF_KPH', 'RF_KPH', 'LR_KPH', 'RR_KPH']):
            influx_data_lines.append(self.buildWheelSpeed(data_state) + str(influx_timestamp))
        if fields.issuperset(['Sport_Mode', 'Pasm_Sport_Mode', 'PSM_Disable']):
            influx_data_lines.append(self.buildPModes(data_state) + str(influx_timestamp))
        return influx_data_lines

    def formatTimeIncrement(self, data_state):
        return None
        
    def formatFooter(self, data_state):
        return None
        
    def buildLocation(self, data):
        #location,vin=<vin>,lap=<lap>,geohash=<geohash> latitude=<999.999999>,longitude=<999.99999>,altitude=<9999>  <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Latitude), DataState.get_data_name_at_idx(DataState.names.Longitude)]
        data.clean_fields(field_names)
        return "location,{0},lap={1},geohash={2} latitude={3},longitude={4},altitude={5} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            '00000000',
            data.get_data_item(DataState.names[DataState.names.Latitude]),
            data.get_data_item(DataState.names[DataState.names.Longitude]),
            data.get_data_item(DataState.names[DataState.names.Altitude]))
    
    def buildAcceleration(self, data):
        #acceleration,vin=<vin>,lap=<lap> x=<xg>,y=<yg>,z=<zg> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.X), 
                       DataState.get_data_name_at_idx(DataState.names.Y), 
                       DataState.get_data_name_at_idx(DataState.names.Z)]
        data.clean_fields(field_names)
        return "acceleration,{0},lap={1} x={2},y={3},z={4} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.X]),
            data.get_data_item(DataState.names[DataState.names.Y]),
            data.get_data_item(DataState.names[DataState.names.Z]))
    
    def buildSteering(self, data):
        #steering,vin=<vin>,lap=<lap> angle=<99999>,rate=<99999> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Steering_Angle),
                       DataState.get_data_name_at_idx(DataState.names.Steering_Rate)]
        data.clean_fields(field_names)
        return "steering,{0},lap={1} angle={2},rate={3} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Steering_Angle]),
            data.get_data_item(DataState.names[DataState.names.Steering_Rate]))
    
    def buildThrottle(self, data):
        #throttle,vin=<vin>,lap=<lap> driver=<999>,ecu=<999> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Throttle),
                       DataState.get_data_name_at_idx(DataState.names.ECU_Throttle)]
        data.clean_fields(field_names)
        return "throttle,{0},lap={1} driver={2},ecu={3} ".format( 
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Throttle]),
            data.get_data_item(DataState.names[DataState.names.ECU_Throttle]))
    
    def buildBrake(self, data):
        #brake,vin=<vin>,lap=<lap> applied=[0/1],pressure=<999> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Brake), 
                       DataState.get_data_name_at_idx(DataState.names.Brake_Pressure)]
        data.clean_fields(field_names)
        return "brake,{0},lap={1} applied={2},pressure={3} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Brake]),
            data.get_data_item(DataState.names[DataState.names.Brake_Pressure]))
    
    def buildClutch(self, data):
        #clutch,vin=<vin>,lap=<lap> released=[0/1] <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Clutch)]
        data.clean_fields(field_names)
        return "clutch,{0},lap={1} released={2} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Clutch]))
    
    def buildRPM(self, data):
        #rpm,vin=<vin>,lap=<lap> value=<9999> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.RPM)]
        data.clean_fields(field_names)
        return "rpm,{0},lap={1} value={2} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.RPM]))
    
    def buildCoolant(self, data):
        #coolant_temperature,vin=<vin>,lap=<lap> value=<coolant-temperature> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Coolant_Temperature)]
        data.clean_fields(field_names)
        return "coolant_temperature,{0},lap={1} value={2} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Coolant_Temperature]))
    
    def buildOilPressure(self, data):
        #oil_pressure,vin=<vin>,lap=<lap> value=<oil-pressure> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Oil_Pressure)]
        data.clean_fields(field_names)
        return "oil_pressure,{0},lap={1} value={2} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Oil_Pressure]))
    
    def buildOilTemperature(self, data):
        #oil_temperature,vin=<vin>,lap=<lap> value=<oil-temperature> <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Oil_Temperature)]
        data.clean_fields(field_names)
        return "oil_temperature,{0},lap={1} value={2} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Oil_Temperature]))
    
    def buildWheelSpeed(self, data):
        #c<timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.LF_KPH),
                       DataState.get_data_name_at_idx(DataState.names.RF_KPH),
                       DataState.get_data_name_at_idx(DataState.names.LR_KPH),
                       DataState.get_data_name_at_idx(DataState.names.RR_KPH)]
        data.clean_fields(field_names)        
        return "wheel_speed,{0},lap={1} left_front={2},right_front={3},left_rear={4},right_rear={5} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.LF_KPH]),
            data.get_data_item(DataState.names[DataState.names.RF_KPH]),
            data.get_data_item(DataState.names[DataState.names.LR_KPH]),
            data.get_data_item(DataState.names[DataState.names.RR_KPH]))
    
    def buildPModes(self, data):
        #pmodes,vin=<vin>,lap=<lap> sport=[0/1],pasm_sport=[0/1],psm_off=[0/1] <timestamp>
        field_names = [DataState.get_data_name_at_idx(DataState.names.Sport_Mode),
                       DataState.get_data_name_at_idx(DataState.names.Pasm_Sport_Mode),
                       DataState.get_data_name_at_idx(DataState.names.PSM_Disable)]
        data.clean_fields(field_names)
        return "pmodes,{0},lap={1} sport={2},pasm_sport={3},psm_off={4} ".format(
            self.tags,
            data.get_data_item(DataState.names[DataState.names.Lap]),
            data.get_data_item(DataState.names[DataState.names.Sport_Mode]),
            data.get_data_item(DataState.names[DataState.names.Pasm_Sport_Mode]),
            data.get_data_item(DataState.names[DataState.names.PSM_Disable]))
