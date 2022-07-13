import logging

from homeassistant.core import HomeAssistant
import time
from peaqevcore.chargertype_service.models.servicecalls_dto import ServiceCallsDTO
from peaqevcore.chargertype_service.models.servicecalls_options import ServiceCallsOptions
from peaqevcore.models.chargerstates import CHARGERSTATES

from peaqevcore.chargertype_service.chargertype_base import ChargerBase
from peaqevcore.chargertype_service.models.calltype import CallType
from custom_components.peaqev.peaqservice.util.constants import (
    CURRENT,
)
import custom_components.peaqev.peaqservice.chargertypes.entitieshelper as helper

_LOGGER = logging.getLogger(__name__)

ENTITYENDINGS = []
NATIVE_CHARGERSTATES = []
DOMAINNAME = "keba"
UPDATECURRENT = True
UPDATECURRENT_ON_TERMINATION = True #might need to change this one.
#docs: https://github.com/home-assistant/core/tree/dev/homeassistant/components/keba


class Keba(ChargerBase):
    def __init__(self, hass: HomeAssistant, chargerid):
        super().__init__(hass)
        self._hass = hass
        self._chargerid = chargerid
        self.options.powerswitch_controls_charging = False
        self.domainname = DOMAINNAME
        self.entities.imported_entityendings = ENTITYENDINGS
        self.native_chargerstates = NATIVE_CHARGERSTATES
        self.chargerstates[CHARGERSTATES.Idle] = []
        self.chargerstates[CHARGERSTATES.Connected] = []
        self.chargerstates[CHARGERSTATES.Charging] = []
        self.chargerstates[CHARGERSTATES.Done] = []

        entitiesobj = helper.getentities(
            self._hass,
            helper.EntitiesPostModel(
                self.domainname,
                self.entities.entityschema,
                self.entities.imported_entityendings
            )
        )
        self.entities.imported_entities = entitiesobj.imported_entities
        self.entities.entityschema = entitiesobj.entityschema

        self.set_sensors()

        _on = CallType("enable", {})
        _off = CallType("disable", {})

        self._set_servicecalls(
            domain=DOMAINNAME,
            model=ServiceCallsDTO(
                on=_on,
                off=_off,
                update_current=CallType("set_current", {CURRENT: "current"})
            ),
            options=ServiceCallsOptions(
                allowupdatecurrent=UPDATECURRENT,
                update_current_on_termination=UPDATECURRENT_ON_TERMINATION
            )
        )

    def getentities(self, domain: str = None, endings: list = None):
        if len(self.entities.entityschema) < 1:
            domain = self.domainname if domain is None else domain
            endings = self.entities.imported_entityendings if endings is None else endings

            entities = helper.get_entities_from_hass(self._hass, domain)

            if len(entities) < 1:
                _LOGGER.error(f"no entities found for {domain} at {time.time()}")
            else:
                _endings = endings
                candidate = ""

                for e in entities:
                    splitted = e.split(".")
                    for ending in _endings:
                        if splitted[1].endswith(ending):
                            candidate = splitted[1].replace(ending, '')
                            break
                    if len(candidate) > 1:
                        break

                self.entities.entityschema = candidate
                _LOGGER.debug(f"entityschema is: {self.entities.entityschema} at {time.time()}")
                self.entities.imported_entities = entities

    def set_sensors(self):
         self.entities.powermeter = f"sensor.{self.entities.entityschema}_charging_power"
         self.entities.powerswitch = f"binary_sensor.{self.entities.entityschema}_state"
         #self.chargerentity = f"sensor.{self._entityschema}_1"
         self.entities.ampmeter = f"sensor.{self.entities.entityschema}_max_current"
         self.options.ampmeter_is_attribute = False
