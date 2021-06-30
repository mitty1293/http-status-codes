from types import MappingProxyType

class HTTPStatusCode():
    def __init__(self):
            self.status_line = MappingProxyType({
                100:"Continue",
                200:"OK",
                400:"Bad Request",
                401:"Unauthorized",
                403:"Forbidden",
                404:"Not Found",
                500:"Internal Server Error",
                501:"Not Implemented",
                502:"Bad Gateway",
                503:"Service Unavailable",
                504:"Gateway Timeout",
                505:"HTTP Version Not Supported"
            })

