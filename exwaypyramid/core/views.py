from pyramid.exceptions import NotFound
from pyramid.response import Response


def home(request):
    return Response('Exway!')


def expenses(request):
    if request.method == 'GET':
        return Response('Nothing here yet!')

    raise NotFound()
