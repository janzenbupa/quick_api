from SquidAPI import SquidAPI
import os

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
    app = create_app()
    from werkzeug import run_simple

    run_simple("127.0.0.1", 5000, app, use_debugger=True, use_reloader=True)

if __name__ == '__main__':
    main()
