import analogio as _aio

AnalogIn = _aio.AnalogIn


class AnalogLightSensor:
    def __init__(self, pin: AnalogIn):
        self.__pin = pin

    def read(self) -> int:
        """The value on the analog pin between 0 and 65535 inclusive (16-bit)."""
        return self.__pin.value

    def reference_voltage(self) -> float:
        """The maximum voltage measurable (also known as the reference voltage) in Volts."""
        return self.__pin.reference_voltage
