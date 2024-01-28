""".....This is facade Design Pattern...."""

class Sensor(object):
    def __init__(self) -> None:
        pass
    def sensor_On(self)->None:
        print("Sensor is On:")
    
    def sensor_of(self)->None:
        print("Sensor is Off:")
    

class Smoke(object):
    def __init__(self) -> None:
        pass
    def smoke_on(self)->None:
        print("smoke is On:")
    
    def smoke_of(self)->None:
        print("smoke is Off:")

class Lights(object):
    def __init__(self) -> None:
        pass
    def lights_on(self)->None:
        print("lights is On:")
        
    def lights_of(self)->None:
        print("lights is off:")
        
        
class Facade(object):
    def __init__(self) -> None:
        self._senor = Sensor()
        self._smoke = Smoke()
        self._light = Lights()
        
    def Emergency(self):
        self._senor. sensor_On()
        self._smoke. smoke_on()
        self._light. lights_on()
    
    def NoEmergency(self):
        self._senor. sensor_of()
        self._smoke. smoke_of()
        self._light. lights_of()
    
    
if __name__ == "__main__":
    facade = Facade()
    sensor = 22
    if sensor >60:
        facade.Emergency()
    else:
        facade.NoEmergency()
        