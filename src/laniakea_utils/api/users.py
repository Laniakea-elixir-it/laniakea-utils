import json, requests
import subprocess
import shlex
import pwd

from flask import Flask, abort, jsonify, request, Blueprint

from laniakea_utils.common.read_config import ReadConfigurationFile
configuration = ReadConfigurationFile()

from laniakea_utils.common.log_facility import LogFacility
log_facility = LogFacility()
logger = log_facility.get_logger()

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/laniakea-utils-api/v1.0/users/info')
def info():
    return "<p>Laniakea Utils: add/remove linux users api</p>"

@users_bp.route('/laniakea-utils-api/v1.0/users/add-user', methods=['POST'])
def add_user():
  # check if user exists, if not create it.
  user = request.json['user']
  try:
    pwd.getpwnam(user)
  except KeyError:
    return jsonify({user: 'already exist' })



#______________________________________
def exec_cmd(cmd):

  proc = subprocess.Popen( shlex.split(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
  communicateRes = proc.communicate()
  stdOutValue, stdErrValue = communicateRes
  status = proc.wait()
  return status, stdOutValue, stdErrValue
