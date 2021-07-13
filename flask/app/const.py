from types import MappingProxyType

class HTTPStatusCode():
    def __init__(self):
            self.status_line = MappingProxyType({
                100:"Continue",
                101:"Switching Protocols",
                102:"Processing",
                103:"Early Hints",
                200:"OK",
                201:"Created",
                202:"Accepted",
                203:"Non-Authoritative Information",
                204:"No Content",
                205:"Reset Content",
                206:"Partial Content",
                300:"Multiple Choice",
                301:"Moved Permanently",
                302:"Found",
                303:"See Other",
                304:"Not Modified",
                400:"Bad Request",
                401:"Unauthorized",
                403:"Forbidden",
                404:"Not Found",
                408:"Request Timeout",
                418:"I'm a teapot",
                500:"Internal Server Error",
                501:"Not Implemented",
                502:"Bad Gateway",
                503:"Service Unavailable",
                504:"Gateway Timeout",
                505:"HTTP Version Not Supported"
            })

