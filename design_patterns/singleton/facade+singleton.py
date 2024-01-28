class Sensor(object):
    def __init__(self) -> None:
        pass

    def sensor_on(self) -> None:
        print("Sensor is On:")

    def sensor_off(self) -> None:
        print("Sensor is Off:")

class Smoke(object):
    def __init__(self) -> None:
        pass

    def smoke_on(self) -> None:
        print("Smoke is On:")

    def smoke_off(self) -> None:
        print("Smoke is Off:")

class Lights(object):
    def __init__(self) -> None:
        pass

    def lights_on(self) -> None:
        print("Lights is On:")

    def lights_off(self) -> None:
        print("Lights is Off:")

class Meta(type):
    """Singleton design pattern."""
    _instance = {}

    def __call__(cls, *args, **kwargs):
        """Creating object"""
        if cls not in cls._instance:
            cls._instance[cls] = super(Meta, cls).__call__(*args, **kwargs)
        return cls._instance[cls]

class Facade(metaclass=Meta):
    def __init__(self) -> None:
        self._sensor = Sensor()
        self._smoke = Smoke()
        self._light = Lights()

    def emergency(self):
        self._sensor.sensor_on()
        self._smoke.smoke_on()
        self._light.lights_on()

    def no_emergency(self):
        self._sensor.sensor_off()
        self._smoke.smoke_off()
        self._light.lights_off()

if __name__ == "__main__":
    facade = Facade()
    # facade.emergency()
    # facade.no_emergency()
    facade1 = Facade()
    print(f"Printing Object: {facade1}")
