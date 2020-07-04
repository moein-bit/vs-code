import requests

r = requests.get("http://sicoms.surge.sh/")
print(r.status_code)
print(r.ok)
# "python.pythonPath": "C:\\Users\\sadra\\.conda\\envs\\pytorch-env\\python.exe",
