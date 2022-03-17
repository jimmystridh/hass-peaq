from enum import Enum

CHARGECONTROLLER = Enum("chargestate", "Idle Start Stop Done Error")
CURRENTS = {3600: 16,3200: 14,2700: 12,	2300: 10,1800: 8,1300: 6}
CURRENTS_3_PHASE = {11000: 16,9600: 14,8200: 12,6900: 10,5500: 8,4100: 6}

#MOCKS BELOW
"""Mock Charger"""
CHARGER = {
    "state": "Available",
}

"""Mock Charger Switch"""
CHARGERSWITCH = {
    "state": "off",
    "current_power": 0,
    "max_current": 6
}


CHARGERTYPE_CHARGEAMPS = "Chargeamps"
CHARGERTYPE_EASEE = "Easee"

LOCALE_SE_GOTHENBURG = "Gothenburg, Sweden"
LOCALE_SE_KARLSTAD = "Karlstad, Sweden"
LOCALE_SE_KRISTINEHAMN = "Kristinehamn, Sweden"
LOCALE_SE_NACKA = "Nacka, Sweden"
LOCALE_SE_PARTILLE = "Partille, Sweden"

"""Expose as options"""
CHARGERTYPES = [
    CHARGERTYPE_CHARGEAMPS, 
    CHARGERTYPE_EASEE
    ]

"""Expose as options"""
LOCALES = [
    LOCALE_SE_GOTHENBURG,
    LOCALE_SE_KARLSTAD,
    LOCALE_SE_KRISTINEHAMN,
    LOCALE_SE_NACKA,
    LOCALE_SE_PARTILLE
    ]


