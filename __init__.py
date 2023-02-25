from SquidAPI import SquidAPI
import os

"""
This is a sample for an application. Each application should contain an __init__.py file
which will instantiate the SquidAPI object. 
"""

def create_app():
    name = __name__
    file = __file__

    app = SquidAPI()

    @app.route("/")
    def hello():
        return None

    @app.route("/<name>")
    def hello_second(name):
        return None

    return app

def main():
    app = create_app()=
    from run_app.run_app import run_app
    run_app("127.0.0.1", 5000, app, use_debugger=True, use_reloader=True)
    

if __name__ == '__main__':
    main()
