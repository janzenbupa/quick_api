from werkzeug import routing
from werkzeug.routing import Rule, Map
from functools import wraps
import typing as t
from functools import update_wrapper

# from . import typing as ft

F = t.TypeVar("F", bound=t.Callable[..., t.Any])

# T_route = t.TypeVar("T_route", bound=ft.RouteCallable)

def setupmethod(f: F) -> F:
    f_name = f.__name__

    def wrapper_func(self, *args: t.Any, **kwargs: t.Any) -> t.Any:
        self._check_setup_finished(f_name)
        return f(self, *args, **kwargs)

    return t.cast(F, update_wrapper(wrapper_func, f))


class Routing():

    def __init__(self):
        self.url_map = Map([])


    @setupmethod
    def route(self, rule: str, file: str, **options: t.Any):
        
        def decorator(f):
            endpoint = options.pop("endpoint", None)
            if endpoint is None:
                endpoint =  file + '\\' + f.__name__
            self.add_url_rule(rule, endpoint, f, **options)
            return f

        return decorator

    def add_url_rule(self, rule: str, method: str, f, **options):
        self.url_map.add(Rule(rule, endpoint=method))

        return None

    def _check_setup_finished(self, f_name: str) -> None:
        return None

    