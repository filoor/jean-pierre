# jeanpierre
**[Prototype]** A Raspberry Pi robot that helps people make their grocery list.

**Work in progress**

[![Build Status](https://travis-ci.org/matteocargnelutti/jean-pierre.svg?branch=master)](https://travis-ci.org/matteocargnelutti/jean-pierre)

# Current version :
* v0.1 - "Baguette"

# Hardware used
* Raspberry Pi Zero W
* Raspberry Pi Camera Module V2
* A random *buzzer* module

# Setup
* Please run *install.sh* : `chmod a+x install.sh` then `./install.sh`

# Processes
**Jean-Pierre is made of three separate processes that are meant to run in parallel.**
* **config** : the configuration assistant.
* **scanner** : Loop that scans the products with the camera.
* **web** : Flask app that handles the web application.

## Manually launch processes
**Processes are automaticaly handled by both supervisor and the install script. But in case you want to launch it separately :**
* `python jeanpierre.py --do config` : launches the configuration assistant.
* `python jeanpierre.py --do scanner` : launches the scanner.
* `python jeanpierre.py --do web` : launches the web app process in debug mode.
* `gunicorn --bind 0.0.0.0 jeanpierre:webapp` : launches the web app process in production mode.

# Database structure
* **Jean-Pierre** uses a SQLite3 database, stored as **database.db** at the project's root.

Table | Use
------| ---
`Params` | Contains config parameters
`Products` | Local products database, contains items scanned and found on OpenFoodFacts, as well as user-created items
`Groceries` | Grocery list, based on the products table


# Shared parameters
Key | Value
----| -----
`buzzer_on` | Should Jean-Pierre try to use a buzzer ?
`buzzer_port` | On which GPIO port the buzzer is ? 
`camera_res_x` | Camera's resolution : width
`camera_res_y` | Camera's resolution : height
`user_password` | Password for the web interface (cyphered)

* Theses parameters are defined using the config assistant, run : `python assistant.py` directly from the **config** subdirectory.
* They are stored into the **Params** database.

# Products data source :
* All products data, including pictures, come from the *OpenFoodFacts API* : https://world.openfoodfacts.org/data

# Dev : PC Mode
* Define an environnement variable `PC_MODE` if you wish to work on this project's code on your PC : it deactivates the import of RPi.GPIO and PiCamera

# Software dependencies
## OS
* Raspbian (lite)

## sudo apt-get install ...
* python3-dev
* python3-pip
* python3-picamera
* git
* virtualenv
* libzbar0
* supervisor
* libjpeg8-dev

## pip dependencies (see requirements.txt)
* picamera
* pyzbar
* pyzbar[scripts]
* pytest
* requests
* RPi.GPIO
* flask
* gunicorn

# Notes to write
* A note about camera focus adjustement (and how it could break the camera)
* A note about the web server security and how it shouldn't be used in production (no https !)