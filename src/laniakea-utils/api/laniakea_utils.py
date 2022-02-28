from flask import Flask
from flask import request
from flaat import Flaat
from flaat import tokentools
import json

flaat = Flaat()
flaat.set_web_framework('flask')

app = Flask(__name__)

# config files
flaat.set_trusted_OP_list([
'https://iam.recas.ba.infn.it/',
'https://cloud-90-147-75-207.cloud.ba.infn.it/'
])


@app.route("/")
@flaat.login_required()
def hello_world():
    return "<p>Hello, World!</p>"

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
