from flask import Flask
from flask import request
from info import info_bp
from galaxyctl import galaxyctl_bp
from users import users_bp
from flaat import Flaat
from flaat import tokentools
import json

import sys
from laniakea_utils.common.read_config import ReadConfigurationFile
from laniakea_utils.common.log_facility import LogFacility

flaat = Flaat()
flaat.set_web_framework('flask')

app = Flask(__name__)
app.register_blueprint(info_bp)
app.register_blueprint(galaxyctl_bp)
app.register_blueprint(users_bp)

configuration = ReadConfigurationFile()
flaat.set_trusted_OP_list(configuration.get_trusted_OP_list())

# this will be unauth.
@app.route("/")
#@flaat.login_required()
def hello_world():
    return "<p>Laniakea Utils API</p>"
