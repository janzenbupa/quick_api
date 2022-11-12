from werkzeug.wrappers import Response


class Endpoints(object):

    def __init__(self):
        self = self

    def hello(self, request):
        return Response("This string came from the Hello file.")

        """
        Each method must return a Response object. 
        """


    def hello_second(self, request, name):

        print(name)
        #name: str = request.args.get("name")
        return Response("Hello, " + name)
