import logging

from homeassistant.core import HomeAssistant
from peaqevcore.models.chargerstates import CHARGERSTATES

from custom_components.peaqev.peaqservice.chargertypes.calltype import CallType
from custom_components.peaqev.peaqservice.chargertypes.chargerbase import ChargerBase
from custom_components.peaqev.peaqservice.util.constants import (
    CURRENT,
)

_LOGGER = logging.getLogger(__name__)

ENTITYENDINGS = []
NATIVE_CHARGERSTATES = []
DOMAINNAME = "keba"
UPDATECURRENT = True
#docs: https://github.com/kirei/hass-chargeamps


class Keba(ChargerBase):
    def __init__(self, hass: HomeAssistant, chargerid):
        super().__init__(hass)
        self._hass = hass
        self._chargerid = chargerid
        self._chargeamps_connector = 1
        self._domainname = DOMAINNAME
        self._entityendings = ENTITYENDINGS

        self._native_chargerstates = NATIVE_CHARGERSTATES
        self._chargerstates[CHARGERSTATES.Idle] = []
        self._chargerstates[CHARGERSTATES.Connected] = []
        self._chargerstates[CHARGERSTATES.Charging] = []

        self.getentities()
        self.set_sensors()

        servicecall_params = {}
        servicecall_params[CURRENT] = "current"

        _on_off_params = { }

        _on = CallType("enable", _on_off_params)
        _off = CallType("disable", _on_off_params)

        self._set_servicecalls(
            domain=DOMAINNAME,
            on_call=_on,
            off_call=_off,
            allowupdatecurrent= UPDATECURRENT,
            update_current_call="set_current",
            update_current_params=servicecall_params
        )

    def set_sensors(self):
         self.powermeter = f"sensor.{self._entityschema}_charging_power"
         self.powerswitch = f"binary_sensor.{self._entityschema}_state"
         #self.chargerentity = f"sensor.{self._entityschema}_1"
         self.ampmeter = f"sensor.{self._entityschema}_max_current"
         self.ampmeter_is_attribute = False

    def _determine_entities(self):
        ret = []
        for e in self._entities:
            entity_state = self._hass.states.get(e)
            if entity_state != "unavailable":
                ret.append(e)
        return ret


    def _determine_switch_entity(self):
        ent = self._determine_entities()
        for e in ent:
            if e.startswith("switch."):
                amps = self._hass.states.get(e).attributes.get("max_current")
                if isinstance(amps, int):
                    return e
        raise Exception
