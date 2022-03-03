from flask import Blueprint

info_bp = Blueprint('info_bp', __name__)

@info_bp.route('/info')
def info():
    return "<p>This is an example blueprintt</p>"


##def info():
##    access_token = tokentools.get_access_token_from_request(request)
##    info = flaat.get_info_thats_in_at(access_token)
##    # FIXME: Also display info from userinfo endpoint
##    x = json.dumps(info, sort_keys=True, indent=4, separators=(',', ': '))
##    return(str(x))
##    return("yeah")
##
##
##@app.route('/valid_user/<id>', methods=['GET'])
##@flaat.login_required()
##def valid_user_id(id):
##    access_token = tokentools.get_access_token_from_request(request)
##    info = flaat.get_info_thats_in_at(access_token)
##    # FIXME: Also display info from userinfo endpoint
##    retval=""
##    if id == info['body']['sub']:
##      retval += F'This worked: there was a valid login, and an id: {id}\n'
##    else:
##      retval += F'This failed'
##
##    return(retval)
##
##@app.route('/valid_user')
##@flaat.login_required()
##def valid_user():
##    return('This worked: there was a valid login\n')
