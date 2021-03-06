![logo](https://raw.githubusercontent.com/matteocargnelutti/jeanpierre/master/misc/ban.png)
# Docs : Dev guide
-- [**Back to README**](http://github.com/matteocargnelutti/jeanpierre)

# About this document
This document give a bit of info about how Jean-Pierre is made, in order to allow people to make it better.

# Processes
**Jean-Pierre is made of three separate processes that are meant to run in parallel.**
* **config** : the configuration assistant.
* **scanner** : Process that scans the products with the camera.
* **web** : Flask app that handles the web application, launched through *gunicorn*.

**Theses processes are launched by supervisor, which has been configured by install.sh** : please see **install.sh** for more info.

## Manually launch processes
**Processes are automaticaly handled by supervisor. But in case you wanted to launch it separately :**
* `./jeanpierre.py --do config` : launches the configuration assistant.
* `./jeanpierre.py --do scanner` : launches the scanner. *Shortcut :* `./scanner.sh`
* `./jeanpierre.py --do webdebug` : launches the web app process in DEBUG mode.
* `gunicorn --bind 0.0.0.0 jeanpierre:webapp` : launches the web app process in production mode. *Shortcut :* `./web.sh`

**You will need to be in the virtual environment context in order to make them work :**
`source env/bin/activate`

# Code structure

## Root directory
File | Use
---- | ---
`jeanpierre.py` | Main entry point with parameters. Also holds a link to the Flask's WSGI constant.
`requirements.txt` | Python dependencies list, used by **install.sh** to manage them
`install.sh` | Install script
`uninstall.sh` | Uninstall script
`sass.sh` | Launches **Sass** to "compile" SCSS files into a single CSS
`scanner.sh` | Shortcut to `./jeanpierre.py --do scanner`
`web.sh` | Shortcut to `gunicorn --bind 0.0.0.0 jeanpierre:webapp`
`database.db` | SQLite3 database file, generated by Jean-Pierre
`flask_secret_key` | Flask encryption key, generated by Jean-Pierre

## Env
This folder, generated by **install.sh**, contains the virtual environment used by the app.

Use `source env/bin/activate` to start it.

## Assets
File | Use
---- | ---
`lang/` | Lang files. Duplicate and rename **en.json** to make Jean-Pierre available for your language !
`static/` | Static files
`static/css/` | CSS files generated by Sass
`static/scss/` | SCSS files to generate CSS
`static/img/` | Web interface images
`static/js/` | Web interface Javascript files
`static/products/` | This folder contains product's pictures grabbed from OpenFoodFacts by the scanner process.
`templates/` | HTML templates used by Flask for the web interface

## Controllers
This folder contains **controllers**, classes used to launch and control specific parts of the app.

Except for **web**, theses controllers holds a **main class** with a static **execute** method, and are called by **jeanpierre.py**.

File | Use
---- | ---
`config.py` | Configuration assistant
`scanner.py` | Scanner
`web.py` | Web interface : this is a Flask app, hence it respects its recommended structure **(list of functions with decorators)**.

## Models
This folder contains **models**, classes used to interact with the database

File | Use
---- | ---
`groceries.py` | *Grocery* table, used for the grocery list.
`params.py` | *Params* table, used for the configuration settings.
`products.py` | *Products* table, used for storing products info.

## Utils
This folder contains **utils**, utilitary classes used by many parts of the program to handle specific tasks.

File | Use
---- | ---
`buzzer.py` | Allows to make the buzzer ring if configured
`database.py` | Used to connect and interact with the SQLite3 database. Has a test mode.
`findproducts.py` | Utilitary used by the scanner to fetch and store information about products. Threaded.
`lang.py` | Handles language files.

## Tests
This folder contains **tests**, classes used for unit testing.

Launch **pytest** to execute the tests.

# Database
## Structure
* **Jean-Pierre** uses a SQLite3 database, stored as **database.db** at the project's root, created by the **configuration assistant**.

Table | Use
------| ---
`Params` | Contains config parameters
`Products` | Local products database, contains items scanned and found on OpenFoodFacts, as well as user-created items
`Groceries` | Grocery list, based on the products table

# Configuration settings
**Configuration settings are stored in the Params table :**

Key | Value
----| -----
`lang` | Interface language
`buzzer_on` | Should Jean-Pierre try to use a buzzer ?
`buzzer_port` | On which GPIO port the buzzer is ? 
`camera_res_x` | Camera's resolution : width
`camera_res_y` | Camera's resolution : height
`user_password` | Password for the web interface (cyphered)

* Theses parameters are defined using the config assistant : `python jeanpierre.py --do config`.

# PC Mode
As it is not possible to import picamera or RPi.GPIO Python libraries on PC, you'll have to define the following **environment variable** to let Jean-Pierre know it shouldn't import them.

`PC_MODE=1`

This is usefull for working on the web interface for example, where theses libs are not necessary.


# Contributing
I would be glad that **Jean-Pierre** continues to improve and evolve : don't hesitate to contribute :) !
