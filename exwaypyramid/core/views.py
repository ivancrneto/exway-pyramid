from pyramid.exceptions import NotFound
from pyramid.renderers import render_to_response
from pyramid.response import Response
import datetime


def home(request):
    return Response('Exway!')


def expenses(request):
    if request.method == 'GET':
        context = {
            'user': 'John',
            'expenses': [
                {
                    'created': datetime.datetime(2015, 2, 21, 10, 00),
                    'description': 'Some dog food',
                    'amount': 20.00,
                    'comment': 'No comments'
                },
                {
                    'created': datetime.datetime(2015, 2, 21, 12, 30),
                    'description': 'My lunch',
                    'amount': 40.00,
                    'comment': 'It was delicious'
                }
            ]
        }
        return render_to_response(
            'core:templates/expenses.jinja2', context, request)

    raise NotFound()
