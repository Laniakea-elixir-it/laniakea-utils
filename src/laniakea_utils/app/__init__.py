from flask import Flask
from flask import request
from flaat.flask import Flaat
import json

import sys
from app.common.read_config import ReadConfigurationFile
from app.common.log_facility import LogFacility

flaat = Flaat()

# verbosity:
#     0: Errors
#     1: Warnings
#     2: Infos
#     3: Debug output
flaat.set_verbosity(3)

app = Flask(__name__)

configuration = ReadConfigurationFile()

flaat.init_app(app)
with app.app_context():
  flaat.set_trusted_OP_list(configuration.get_trusted_OP_list())

from app.info import info_bp
app.register_blueprint(info_bp)

from app.galaxyctl import galaxyctl_bp
app.register_blueprint(galaxyctl_bp)

from app.os_users_manager import users_bp
app.register_blueprint(users_bp)


# -------------------------------------------------------------------
# This will be unauth -----------------------------------------------
@app.route("/")
def root():
    return "<p>Laniakea Utils API</p>"

# -------------------------------------------------------------------
# Endpoint which requires of an authenticated user ------------------
@app.route("/authenticated", methods=["GET"])
@flaat.is_authenticated()
def authenticated():
    return "This worked: there was a valid login"
