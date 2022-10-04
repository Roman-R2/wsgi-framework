class PageNotFound404:
    def __call__(self, request, *args, **kwargs):
        return '404 WHAT', '404 Page Not Found'


class Framework:
    """ Main class for framework. """

    def __init__(self, routes_obj, fronts_obj):
        self.routes_lst = routes_obj
        self.fronts_lst = fronts_obj

    def __call__(self, environ, start_response):
        # Get current  url
        path = environ['PATH_INFO']

        # Add end slash in url
        if not path.endswith('/'):
            path = f'{path}/'

        # Find neaded controller (page controller pattern)
        if path in self.routes_lst:
            view = self.routes_lst[path]
        else:
            view = PageNotFound404()
        request = {}

        # Add elements to request dict
        # request dict get all controllers (front controller pattern)
        for front in self.fronts_lst:
            front(request)

        # Run controller with request object
        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
