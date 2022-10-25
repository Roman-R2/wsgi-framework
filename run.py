from wsgiref.simple_server import make_server

from r2_framework.main import Framework
from urls import fronts
from views import routes

DEFAULT_PORT = 8080

application = Framework(routes, fronts)

with make_server('', DEFAULT_PORT, application) as httpd:
    print(f'Server runing on port {DEFAULT_PORT}')
    print(f'http://127.0.0.1:{DEFAULT_PORT}')
    httpd.serve_forever()
