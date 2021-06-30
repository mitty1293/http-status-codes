from types import MappingProxyType

class HTTPStatusCode():
    def __init__(self):
            self.status_line = MappingProxyType({
                200:"OK",
                403:"Forbidden",
                404:"Not Found",
                500:"Internal Server Error"
            })

