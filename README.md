## Synopsis
A python based RESTful API for Walabot devices

## Motivation
Well, I was working on a project to have my Walabot emulate a variety of
musical instruments from the browser. After searching around I couldn't
find any web apis set up yet so I figured we should start one.

## Installation
* Ensure the [Walabot python sdk](https://walabot.com/getting-started) is installed and configured properly
* pip install flask flask-cors flask-autodoc Flask-Testing
* Run python app.py
* In a browser, open http://localhost:5000/walabot/api/v1.0/documentation

## Planned Enhancements
* PATCH operations or headers to configure the Walabot's arena, resolution, etc.
* Tying off the host url, port and other variables in a config file.
* Complete test coverage.

## API Reference
/walabot/api/v1.0/imageenergy
HEAD GET OPTIONS

/walabot/api/v1.0/imagingtargets
HEAD GET OPTIONS

/walabot/api/v1.0/rawimage
HEAD GET OPTIONS

/walabot/api/v1.0/rawimageslice
HEAD GET OPTIONS

/walabot/api/v1.0/sensortargets
HEAD GET OPTIONS

/walabot/api/v1.0/status
HEAD GET OPTIONS

/walabot/api/v1.0/threshold
HEAD GET OPTIONS

/walabot/api/v1.0/version
HEAD GET OPTIONS
