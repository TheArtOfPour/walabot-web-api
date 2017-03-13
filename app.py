from __future__ import print_function
import importlib.machinery
import importlib.util
from flask import Flask, jsonify
from flask_cors import CORS
from flask.ext.autodoc import Autodoc

host = 'localhost'
walabotAPIPath = 'C:/Program Files/Walabot/WalabotSDK/python/WalabotAPI.py'
loader = importlib.machinery.SourceFileLoader('WalabotAPI', walabotAPIPath)
spec = importlib.util.spec_from_loader(loader.name, loader)
WalabotAPI = importlib.util.module_from_spec(spec)
loader.exec_module(WalabotAPI)
WalabotAPI.Init()
WalabotAPI.SetSettingsFolder()

app = Flask(__name__)
CORS(app)
auto = Autodoc(app)


@app.before_request
def before_request():
    WalabotAPI.ConnectAny()
    WalabotAPI.SetProfile(WalabotAPI.PROF_SHORT_RANGE_IMAGING)
    WalabotAPI.SetDynamicImageFilter(WalabotAPI.FILTER_TYPE_NONE)
    WalabotAPI.Start()
    WalabotAPI.StartCalibration()
    WalabotAPI.Trigger()


@app.after_request
def after_request(response):
    WalabotAPI.Stop()
    WalabotAPI.Disconnect()
    return response


@app.route('/walabot/api/v1.0/imageenergy', methods=['GET'])
@auto.doc()
def get_image_energy():
    return jsonify({'imageenergy': WalabotAPI.GetImageEnergy()})


@app.route('/walabot/api/v1.0/imagingtargets', methods=['GET'])
@auto.doc()
def get_imaging_targets():
    return jsonify({'imagingtargets': WalabotAPI.GetImagingTargets()})


@app.route('/walabot/api/v1.0/rawimage', methods=['GET'])
@auto.doc()
def get_raw_image():
    return jsonify({'rawimage': WalabotAPI.GetRawImage()})


@app.route('/walabot/api/v1.0/rawimageslice', methods=['GET'])
@auto.doc()
def get_raw_image_slice():
    return jsonify({'rawimageslice': WalabotAPI.GetRawImageSlice()})


@app.route('/walabot/api/v1.0/sensortargets', methods=['GET'])
@auto.doc()
def get_sensor_targets():
    return jsonify({'sensortargets': WalabotAPI.GetSensorTargets()})


@app.route('/walabot/api/v1.0/status', methods=['GET'])
@auto.doc()
def get_status():
    return jsonify({'status': WalabotAPI.GetStatus()})


@app.route('/walabot/api/v1.0/threshold', methods=['GET'])
@auto.doc()
def get_threshold():
    return jsonify({'threshold': WalabotAPI.GetThreshold()})


@app.route('/walabot/api/v1.0/version', methods=['GET'])
@auto.doc()
def get_version():
    return jsonify({'version': WalabotAPI.GetVersion()})


@app.route('/walabot/api/v1.0/documentation')
def documentation():
    return auto.html()


if __name__ == '__main__':
    app.run(debug=True, host=host)
