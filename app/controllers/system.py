from flask import jsonify, Blueprint
from datetime import datetime

system_bp = Blueprint('system', __name__)


@system_bp.route('/system/time', methods=['GET'])
def get_server_time():
    now = datetime.now()
    return jsonify({'time': now.strftime("%Y-%m-%d %H:%M:%S")})
