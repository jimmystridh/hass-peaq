from abc import abstractmethod
from datetime import datetime
import custom_components.peaqev.peaqservice.util.constants as constants
from peaqevcore.Threshold import ThresholdBase as _core
import logging

_LOGGER = logging.getLogger(__name__)

class ThresholdBase:
    def __init__(self, hub):
        self._hub = hub

    @property
    def stop(self) -> float:
        return _core.stop(
            datetime.now().minute,
            str(datetime.now().hour) in self._hub.hours.caution_hours if self._hub.price_aware is False else False
        )

    @property
    def start(self) -> float:
        return _core.start(
            datetime.now().minute,
            str(datetime.now().hour) in self._hub.hours.caution_hours if self._hub.price_aware is False else False
        )

    @property
    @abstractmethod
    def allowedcurrent(self) -> int:
        pass

    # this one must be done better. Currently cannot accommodate 1-32A single phase for instance.
    def _setcurrentdict(self):
        if 0 < int(self._hub.carpowersensor.value) < 3700:
            return constants.CURRENTS_ONEPHASE_1_16
        return constants.CURRENTS_THREEPHASE_1_16