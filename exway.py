from pyramid.config import Configurator
from wsgiref.simple_server import make_server
from pyramid.response import Response


def home(request):
    return Response('Exway!')


if __name__ == '__main__':
    config = Configurator()
    config.add_route('home', '/')
    config.add_view(home, route_name='home')
    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    print('Server running at: 0.0.0.0:6543')
    server.serve_forever()
