from pyramid.exceptions import NotFound
from pyramid.view import view_config
import datetime


@view_config(route_name='core:views.home', renderer='string')
def home(request):
    return 'Exway!'


@view_config(
    route_name='core:views.expenses',
    renderer='core:templates/expenses.jinja2')
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
        return context

    raise NotFound()
