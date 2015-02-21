from pyramid.config import Configurator
from pyramid.exceptions import NotFound
from pyramid.response import Response
from wsgiref.simple_server import make_server


def home(request):
    return Response('Exway!')


def expenses(request):
    if request.method == 'GET':
        return Response('Nothing here yet!')

    raise NotFound()


if __name__ == '__main__':
    config = Configurator()

    config.add_route('home', '/')
    config.add_view(home, route_name='home')
    config.add_route('expenses', '/expenses')
    config.add_view(expenses, route_name='expenses')

    app = config.make_wsgi_app()

    server = make_server('0.0.0.0', 6543, app)
    print('Server running at: 0.0.0.0:6543')
    server.serve_forever()
