from custom_components.peaq.sensors.sensorbase import SensorBase

from homeassistant.const import (
    DEVICE_CLASS_POWER,
    POWER_WATT,
    DEVICE_CLASS_CURRENT,
    ELECTRIC_CURRENT_AMPERE
)

class PeaqAmpSensor(SensorBase):
    device_class = DEVICE_CLASS_CURRENT
    unit_of_measurement = ELECTRIC_CURRENT_AMPERE
    
    def __init__(self, hub, hass):
        name = f"{hub.NAME} Allowed current"
        super().__init__(hub, name.lower())
        self.hub = hub
        self._state = self.hub.Threshold.AllowedCurrent
        self._attr_icon = "mdi:current-ac"

    @property
    def state(self) -> int:
        return self._state

    def update(self) -> None:
        self._state = self.hub.Threshold.AllowedCurrent


class PeaqPowerSensor(SensorBase):
    device_class = DEVICE_CLASS_POWER
    unit_of_measurement = POWER_WATT
    
    def __init__(self, hub, hass):
        name = f"{hub.NAME} {hub.TotalPowerSensor.Name}"
        super().__init__(hub, name.lower())
        self.hub = hub
        self._state = self.hub.TotalPowerSensor.State
        self._attr_icon = "mdi:flash"

    @property
    def state(self) -> int:
        return self._state

    def update(self) -> None:
        self._state = self.hub.TotalPowerSensor.State