[![hacs_badge](https://img.shields.io/badge/HACS-Default-brightgreen.svg)](https://github.com/hacs/integration) 
![Validate with hassfest](https://github.com/elden1337/hass-peaq/workflows/Validate%20with%20hassfest/badge.svg) 
[![Peaq_downloads](https://img.shields.io/github/downloads/elden1337/hass-peaq/total)](https://github.com/elden1337/hass-peaq) 
[![hass-peaq_downloads](https://img.shields.io/github/downloads/elden1337/hass-peaq/latest/total)](https://github.com/elden1337/hass-peaq)
[![Buy me a coffee](https://img.shields.io/static/v1.svg?label=Buy%20me%20a%20coffee&message=🥨&color=black&logo=buy%20me%20a%20coffee&logoColor=white&labelColor=6f4e37)](https://www.buymeacoffee.com/elden)
[![](https://img.shields.io/github/sponsors/elden1337)](https://github.com/sponsors/elden1337)

# Peaqev ev-charging

<img src="https://raw.githubusercontent.com/elden1337/hass-peaq/main/assets/icon.png" width="125">

### :cherries: Sponsorship and prioritized development :cherries:
Peaqev is developed without static funding. If you lack your locale/chargertype or have wishes for other specific features that you would like to see prioritized, please consider becoming a [Github-sponsor](https://github.com/sponsors/elden1337) to bump your desired changes in my backlog.
- In order to flag a ticket, either create a new one or comment on an existing one after you've started your sponsorship. I will then flag the ticket with `sponsored-change` and try to prioritize this going forward
- Becoming a sponsor is not a guarantee that a wish will be created, or a guarantee for a specified resolution-time. Peaqev is being developed in my sparetime and every feature has to be considered by me before taking it into development
- I may need to reach out for testing, especially if your wish includes implementing new chargertypes
- Critical bugs discovered of course always triages higher than features

:love_letter:

---

Welcome to Peaqev!

This application started as an attempt to lower the household's peak energy charges, targeted at charging an ev below a set threshold. 
Since then, we have evolved, and now offer a broader feature-set including price aware smart charge (a very smart calculation if you ask us), looking ahead at tomorrow's prices automatically, installation without the need for a power meter etc.
Peaqev covers 23 different energy companies in Sweden, Norway and Belgium and two types of ev-chargers _(2021-08-26)_

The integration does not communicate with any properitary API's. However, the chargers selected will use the integrations set for them, and may include cloud polling of data.

For usage-examples and more in-depth explanations, see the Wiki:
* [List of available Locales](https://github.com/elden1337/hass-peaq/wiki/Locale)
* [Price awareness](https://github.com/elden1337/hass-peaq/wiki/Price-awareness)
* [Scheduler](https://github.com/elden1337/hass-peaq/wiki/Scheduler)
* [Usage](https://github.com/elden1337/hass-peaq/wiki/Usage)

## Installation
*Required to install is Home Assistant version 2022.8.0 or higher.*

Preferred if you have HACS installed is to search for Peaqev there.

Otherwise you may:
- Copy `custom_components/peaqev` folder to `<config_dir>/custom_components/peaqev/`
- Restart Home assistant
- Go to Configuration > Devices & Services > Add integration

### Config setup:

Peaqev has two types of installations: Regular and Lite. Regular is much more precise, but requires an installed powersensor while Lite does not.

[![](https://mermaid.ink/img/pako:eNpVkNtqwzAMhl_F-CqD5gVyMRg5NIUMRrO7eRciVhuDYwdFZpSm7z7nUNh0Jen_pB_pLjuvUWbySjD2ojkrJ2K8fbUMxN8iTV9FnpzcxGAtsPFO8G3Elw3LF31uDOMsiiTvga5IApwWje_A_sfOeA0WaBZl0qKbPO1quZoUW1GsRZV8kOkwhR-g55JqXVKBnaLZMal9oGmXjutQ_Zf7pBCxOnn3jvuFU7zJ8iAHpAGMjkffl56S3OOASmYx1XiBYFlJ5R4RDaMGxlIb9iSzy2J-kBDYtzfXyYyjyxMqDMQfDjv1-AUWBWqX)](https://mermaid-js.github.io/mermaid-live-editor/edit#pako:eNpVkNtqwzAMhl_F-CqD5gVyMRg5NIUMRrO7eRciVhuDYwdFZpSm7z7nUNh0Jen_pB_pLjuvUWbySjD2ojkrJ2K8fbUMxN8iTV9FnpzcxGAtsPFO8G3Elw3LF31uDOMsiiTvga5IApwWje_A_sfOeA0WaBZl0qKbPO1quZoUW1GsRZV8kOkwhR-g55JqXVKBnaLZMal9oGmXjutQ_Zf7pBCxOnn3jvuFU7zJ8iAHpAGMjkffl56S3OOASmYx1XiBYFlJ5R4RDaMGxlIb9iSzy2J-kBDYtzfXyYyjyxMqDMQfDjv1-AUWBWqX)

##### Installation type:
- `Installation type` - Pick regular for the full Peaqev-experience. This will charge according to your home's total energy. Pick Lite if you do not have such a sensor installed. Peaqev will then charge the allowed hourly amount set further down in "Months"

##### Sensor:
- `Power sensor` - The already existing power sensor in your setup. This is required to get the reading to work. Examples of devices sending such data is Tibber Pulse/Watty, Shelly DIN-mounted devices or similar.
- `Power sensor includes car` - Check this option if the above sensor includes your car's power draw. The calutions will be altered accordingly

##### Charger and Locale:
- `City, or Grid owner company` - Chose your city from the list. The characteristics differ in how peak hours are stored and measured. If you don't live in a supported location but just want to test the integration, or lower your peaks for other reasons, you may check *"Other, just want to test"*
- `Charger type` - Pick the installed ev-charger you have. Currently Chargeamps, Easee and Outdoor smart outlets are supported. Check links for required custom components per charger-type: [Chargeamps](https://github.com/kirei/hass-chargeamps), [Easee](https://github.com/fondberg/easee_hass/)
- `Charger id` - Your local identifier to tell Peaqev which charger unit we mean to manipulate. If your chargertype does not provide this, leave blank
- *If you have selected Smart outlet as charger type, you will need to provide the switch to turn on/off, and the sensor to read power from the outlet instead of charger id.*

##### Price-aware:
- `Price aware charging` - Check this to calculate the cheapest hours from Nordpool (requires [Nordpool](https://github.com/custom-components/nordpool)). Above Non- and Caution-hours will be ignored.
- `Absolute top price` - The limit (if any) where your charger should be stopped, regardless of the hour-algorithm.
- `Min price` - The lower limit (if any) where charging will always be permitted (must be lower than top-price if set).
- `Caution-hour type` - Choose to what extent you would like Peaqev to hold back during caution-hours. *Suave > Aggressive* 

##### Hours:
- `Non hours` - Click to select the hours (if any) where you do not wish to charge.  
- `Caution hours` - Click to select the hours (if any) where you want the charger to be extra cautious to not break the peak.

##### Months:
- `Monthly allowed peak` - Needs to be set in order to determine a minimum allowed peak. In the beginning of each month this is necessary to be able to charge at all. *Format is in kW. See examples below*


These are two (quite restrained) examples of monthly start peaks, for 1-phase and 3-phase charging respectively. This option is always up to your house and it's other appliances. The below are made for a modern house with installed heat pump.
These suggestions are also made for hourly calculation. Should your Locale apply other, like quarter-hourly, do consider altering the numbers accordingly.

Month | 1-phase charge | 3-phase charge
--- | --- | ---
Jan| 2.0 | 4.0
Feb| 1.8 | 3.6
Mar| 1.8 | 3.6
Apr| 1.5 | 3.0
May| 1.5 | 3.0
Jun| 1.5 | 3.0
Jul| 1.5 | 3.0
Aug| 1.5 | 3.0
Sep| 1.5 | 3.0
Oct| 1.5 | 3.0
Nov| 1.8 | 3.6
Dec| 2.0 | 4.0


*While this integration will try to not break your monthly energy peak hour, there is off course no guarantee. Various factors beyond control of this logic do occur, so for those aiming at staying below their threshold, I do suggest you think about the non-hours, caution-hours etc in the setup. These hours should be set when you commonly utilize a lot of extra energy in your home, such as cooking, doing laundry etc.*

-----

A special thanks to my sponsors! Your support is greatly appreciated. 
- [@mejje](https://github.com/mejje)
