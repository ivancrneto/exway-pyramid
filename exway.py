from pyramid.config import Configurator
from wsgiref.simple_server import make_server


if __name__ == '__main__':
    config = Configurator()
    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    print('Server running at: 0.0.0.0:6543')
    server.serve_forever()
