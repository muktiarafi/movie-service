import sys
import os
import re
import json
from werkzeug.wrappers import Request, Response, ResponseStream
import jwt

sys.path.append('..')
from errors.require_auth import RequireAuthError

class middleware():

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        request = Request(environ)

        if ((request.path, request.method) == ('/api/movies', 'GET')):
            return self.app(environ, start_response)

        cookie_session = request.cookies.get('session')
        
        if not cookie_session:
            err = Response(json.dumps(RequireAuthError().to_dict()), mimetype="application/json", status=401)
            return err(environ, start_response)

        token = re.findall(r'ey[^%]+', cookie_session)
        print(token[0])

        try:
            payload = jwt.decode(token[0], os.environ.get('JWT_KEY'))
            environ['currentuser'] = payload

            return self.app(environ, start_response)
        except jwt.DecodeError as err:
            print(err)

        res = Response(json.dumps(RequireAuthError().to_dict()), mimetype="application/json", status=401)
        return res(environ, start_response)

