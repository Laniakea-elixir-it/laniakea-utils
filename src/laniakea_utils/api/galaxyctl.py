import json, requests
import subprocess
import shlex
import socket
import time

from flask import Flask, abort, jsonify, request, Blueprint

from laniakea_utils.common.read_config import ReadConfigurationFile
configuration = ReadConfigurationFile()

from laniakea_utils.common.log_facility import LogFacility
log_facility = LogFacility()
logger = log_facility.get_logger()

galaxyctl_bp = Blueprint('galaxyctl_bp', __name__)

@galaxyctl_bp.route('/galaxyctl_api/v1.0/info')
def info():
    return "<p>Laniakea Utils: galaxyctl api</p>"

@galaxyctl_bp.route('/galaxyctl_api/v1.0/galaxy-startup', methods=['POST'])
def galaxy_startup():

    # check if galaxy is online, if yes return online
    # else run galaxy-startup script

    if not request.json or not 'endpoint' in request.json:
       abort(400)

    endpoint = request.json['endpoint']

    try:
      response = requests.get(endpoint, verify=False)
    except OSError as e:
      # restart nginx to prevent connection refused
      restart_nginx()
      response = requests.get(endpoint, verify=False)

    sc = str(response.status_code)

    if sc == '200' or sc == '302':
      return jsonify({'galaxy': 'online' }) 

    else:

     return galaxy_startup(endpoint)

#______________________________________
def exec_cmd(cmd):

  proc = subprocess.Popen( shlex.split(cmd), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
  communicateRes = proc.communicate()
  stdOutValue, stdErrValue = communicateRes
  status = proc.wait()
  return status, stdOutValue, stdErrValue

#______________________________________
def galaxy_startup(endpoint):

  command = configuration.get_galaxy_restart_command()

  status, stdout, stderr = exec_cmd(command)

  logger.debug( 'Startup stdout: ' + str(stdout) )
  logger.debug( 'Startup stderr: ' + str(stderr) )
  logger.debug( 'Startup status: ' + str(status) )

  # wait for socket and stats server
  wait_for_port(4010, '127.0.0.1', 50.0) 
  wait_for_port(4001, '127.0.0.1', 50.0)

  # check for galaxy 
  response = requests.get(endpoint, verify=False)
  sc = str(response.status_code)

  if sc == '200' or sc == '302':
     return jsonify({'galaxy': 'online' })

  else:
    return jsonify({'galaxy': 'unavailable'})


#______________________________________
def restart_nginx():

  command = configuration.get_nginx_restart_command()
  status, stdout, stderr = exec_cmd(command)

  logger.debug( 'NGINX restart status: ' + str(status) )
  logger.debug( 'NGINX restart  stdout: ' + str(stdout) )
  logger.debug( 'NGINX stderr: ' + str(stderr) )


#______________________________________
def wait_for_port(port: int, host: str = 'localhost', timeout: float = 5.0):
    """Wait until a port starts accepting TCP connections.
    Args:
        port: Port number.
        host: Host address on which the port should exist.
        timeout: In seconds. How long to wait before raising errors.
    Raises:
        TimeoutError: The port isn't accepting connection after time specified in `timeout`.
    """
    start_time = time.perf_counter()
    while True:
        try:
            with socket.create_connection((host, port), timeout=timeout):
                break
        except OSError as ex:
            time.sleep(0.01)
            if time.perf_counter() - start_time >= timeout:
                raise TimeoutError('Waited too long for the port {} on host {} to start accepting '
                                   'connections.'.format(port, host)) from ex
