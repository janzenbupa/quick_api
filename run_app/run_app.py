
from SquidAPI import SquidAPI
from werkzeug import run_simple
from typing import Type


#Need to add more functionality to this. 
def run_app(host: str, port: int, application: Type[SquidAPI], use_debugger = True,
            use_reloader = True):
    run_simple(host, port, application, use_debugger, use_reloader)
    
