import json

from flask import make_response, request, session, abort
from flask.views import MethodView





class BaseHandler(MethodView):
    """
    Flask Application BaseHandler
    """
    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__()
        self.request = request
        self.session = session


    def set_session(self, key, value):
        self.session[key] = value

    def get_session(self, key):
        return self.session.get(key, None)

    def del_session(self, key):
        return self.session.pop(key, None)

    def clear_session(self):
        self.session.clear()

    @property
    def user_id(self):
        return self.session.get('uid', None)

    @staticmethod
    def write_response(data=None, status=1, error_msg="", http_status=200):
        if data is None:
            data = {}
        _data = {
            "data": data,
            "status": status,
            "message": error_msg,
        }
        _data = json.dumps(_data)
        response = make_response(_data, http_status)
        response.headers['Content-Type'] = 'application/json'
        return response



