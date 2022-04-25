from custom_components.peaqev.sensors.sensorbase import SensorBase
from custom_components.peaqev.peaqservice.util.constants import CHARGERCONTROLLER

class PeaqSensor(SensorBase):
    def __init__(self, hub):
        name = f"{hub.hubname} {CHARGERCONTROLLER}"
        super().__init__(hub, name)

        self._attr_name = name
        self._state = self._hub.chargecontroller.status.name
        self._nonhours = None
        self._cautionhours = None
        self._current_hour = None,
        self._price_aware = False,
        self._absolute_top_price = None

    @property
    def state(self):
        return self._hub.chargecontroller.status.name

    @property
    def icon(self) -> str:
        return "mdi:gate-xor"

    def update(self) -> None:
        self._state = self._hub.chargecontroller.status.name
        self._nonhours = self._hub.hours.non_hours
        self._cautionhours = self._hub.hours.caution_hours
        self._current_hour = self._hub.hours.state
        self._price_aware = self._hub.hours.price_aware
        self._absolute_top_price = self._hub.hours.absolute_top_price if self._price_aware is True else float("inf")

    @property
    def extra_state_attributes(self) -> dict:
        dict = {
            "non_hours": self._nonhours,
            "caution_hours": self._cautionhours,
            "current_hour state": self._current_hour,
            "price aware": self._price_aware,
        }

        if self._price_aware is True:
            dict["absolute top price"] = self._absolute_top_price

        return dict
