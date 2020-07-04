import math
import sys
from os import rename

import requests

# print(sys.version)
print("hello")
print(sys.executable)


def func(arg1, arg2):
    # var = "something"
    return arg1 * arg2


# print("hello world")
r = requests.get("http://sicoms.surge.sh/")
print(r.status_code)
# "python.pythonPath": "C:\\Users\\sadra\\.conda\\envs\\pytorch-env\\python.exe",
