def includeme(config):
    config.add_route('core:views.home', '/')
    config.add_route('core:views.expenses', '/expenses')

    config.scan('core.views')
