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
        influx_timestamp = influxTimestamp(data_state)
        influx_data = None
        if fields.containsAll(['Latitude','Longitude']):
            influx_data = self.buildLocation(data_state)
            data_state.clean_fields(['Latitude','Longitude'])
        elif fields.containsAll(['X','Y','Z']):
            influx_data = self.buildAcceleration(data_state)
            data_state.clean_fields(['X','Y','Z'])
        elif fields.containsAll(['Steering_Angle','Steering_Rate']):
            influx_data = self.buildSteering(data_state)
            data_state.clean_fields(['Steering_Angle','Steering_Rate'])
        elif fields.containsAll(['Throttle','ECU_Throttle']):
            influx_data = self.buildThrottle(data_state)
            data_state.clean_fields(['Throttle','ECU_Throttle'])
        elif fields.containsAll(['Brake','Brake_Pressure']):
            influx_data = self.buildBrake(data_state)
            data_state.clean_fields(['Brake','Brake_Pressure'])
        elif fields.containsAll(['Clutch']):
            influx_data = self.buildClutch(data_state)
            data_state.clean_fields(['Clutch'])
        elif fields.containsAll(['RPM']):
            influx_data = self.buildRPM(data_state)
            data_state.clean_fields(['RPM'])
        elif fields.containsAll(['Coolant_Temperature']):
            influx_data = self.buildCoolant(data_state)
            data_state.clean_fields(['X','Y','Z'])
        elif fields.containsAll(['Coolant_Temperature']):
            influx_data = self.buildOilPressure(data_state)
            data_state.clean_fields(['Oil_Pressure'])
        elif fields.containsAll(['Oil_Temperature']):
            influx_data = self.buildOilTemperature(data_state)
            data_state.clean_fields(['Oil_Temperature'])
        elif fields.containsAll(['LF_KPH','RF_KPH','LR_KPH','RR_KPH']):
            influx_data = self.buildWheelSpeed(data_state)
            data_state.clean_fields(['LF_KPH','RF_KPH','LR_KPH','RR_KPH'])
        elif fields.containsAll(['Sport_Mode','Pasm_Sport_Mode','PSM_Disable']):
            influx_data = self.buildPModes(data_state)
            data_state.clean_fields(['Sport_Mode','Pasm_Sport_Mode','PSM_Disable'])

    def formatTimeIncrement(self, data_state):
        return None
        
    def formatFooter(self, data_state):
        return None
        
    def buildLocation(self, data):
        #location,vin=<vin>,lap=<lap>,geohash=<geohash> latitude=<999.999999>,longitude=<999.99999>,altitude=<9999>  <timestamp>
        influx_data = "location,{0},geohash={1} latitude={2},longitude={3},altitude={4} {5}".format(
            self.tags,
            '00000000',
            data.get_data_item('Latitude'),
            data.get_data_item('Longitude'),
            data.get_data_item('Altitude'),
            influxTimestamp())
        return None
    
    def buildAcceleration(self, data):
        return None
    
    def buildSteering(self, data):
        return None
    
    def buildThrottle(self, data):
        return None
    
    def buildBrake(self, data):
        return None
    
    def buildClutch(self, data):
        return None
    
    def buildRPM(self, data):
        return None
    
    def buildCoolant(self, data):
        return None
    
    def buildOilPressure(self, data):
        return None
    
    def buildOilTemperature(self, data):
        return None
    
    def buildWheelSpeed(self, data):
        return None
    
    def buildPModes(self, data):
        return None