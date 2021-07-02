from types import MappingProxyType

class HTTPStatusCode():
    def __init__(self):
            self.status_line = MappingProxyType({
                100:"Continue",
                102:"Processing",
                200:"OK",
                201:"Created",
                204:"No Content",
                301:"Moved Permanently",
                400:"Bad Request",
                401:"Unauthorized",
                403:"Forbidden",
                404:"Not Found",
                408:"Request Timeout",
                500:"Internal Server Error",
                501:"Not Implemented",
                502:"Bad Gateway",
                503:"Service Unavailable",
                504:"Gateway Timeout",
                505:"HTTP Version Not Supported"
            })

