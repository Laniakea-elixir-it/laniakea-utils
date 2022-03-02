from flask import Flask
from flask import request
from flaat import Flaat
from flaat import tokentools
import json


import sys
from laniakea_utils.common.read_config import ReadConfigurationFile
from laniakea_utils.common.log_facility import LogFacility

flaat = Flaat()
flaat.set_web_framework('flask')

app = Flask(__name__)

configuration = ReadConfigurationFile()
flaat.set_trusted_OP_list(configuration.get_trusted_OP_list())

# this will be unauth.
@app.route("/")
#@flaat.login_required()
def hello_world():
    return "<p>Laniakea Utils API</p>"

@app.route('/info')
def info():
    access_token = tokentools.get_access_token_from_request(request)
    info = flaat.get_info_thats_in_at(access_token)
    # FIXME: Also display info from userinfo endpoint
    x = json.dumps(info, sort_keys=True, indent=4, separators=(',', ': '))
    return(str(x))
    return("yeah")


@app.route('/valid_user/<id>', methods=['GET'])
@flaat.login_required()
def valid_user_id(id):
    access_token = tokentools.get_access_token_from_request(request)
    info = flaat.get_info_thats_in_at(access_token)
    # FIXME: Also display info from userinfo endpoint
    retval=""
    if id == info['body']['sub']:
      retval += F'This worked: there was a valid login, and an id: {id}\n'
    else:
      retval += F'This failed'

    return(retval)

@app.route('/valid_user')
@flaat.login_required()
def valid_user():
    return('This worked: there was a valid login\n')
