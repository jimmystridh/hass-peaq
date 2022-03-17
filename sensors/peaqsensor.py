from custom_components.peaq.sensors.sensorbase import SensorBase

class PeaqSensor(SensorBase):
    def __init__(self, hub):
        name = f"{hub.NAME} ChargerController"
        super().__init__(hub, name.lower())

        self._attr_name = name
        self._state = self._hub.ChargeController.status.name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._hub.ChargeController.status.name

    @property
    def icon(self) -> str:
        return "mdi:gate-xor"