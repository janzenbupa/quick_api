from ast import Str
import imp
from importlib import import_module
import os
from werkzeug.urls import url_parse
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader
import typing as t
from functools import update_wrapper

from Routing import Routing


class SquidAPI(object):

    url_map = None
    # routing: Routing = None


    
    def __init__(self):

        # self.routing = Routing()

        self.url_map = Map([])

        #self.response = Response()

        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),
            autoescape=True)
            

    def wsgi_app(self, environ ,start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)

        print(self.url_map)

        try:
            import Endpoints
            edpt = Endpoints
            import sys
            t = dir(sys.modules[__name__])

            endpoint, values = adapter.match()
            from Endpoints import Endpoints as ep
            endpoint_object = ep.Endpoints()
            return getattr(endpoint_object, f'{endpoint}')(request, **values)

        except HTTPException as e:
            return e


    #routing begin
    def route(self, rule: str, **options: t.Any):
        
        def decorator(f):
            endpoint = options.pop("endpoint", None)
            if endpoint is None:
                endpoint =  f.__name__
            self.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator

    def add_url_rule(self, rule: str, method: str, f, **options):
        self.url_map.add(Rule(rule, endpoint=method))

        return None

    #routing end



    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


    