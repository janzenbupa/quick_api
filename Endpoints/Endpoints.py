from werkzeug.wrappers import Response


class Endpoints(object):

    def __init__(self):
        self = self

    def hello(self, request):
        return Response("This string came from the Hello file.")

        """
        Each method must return a Response object. 
        """