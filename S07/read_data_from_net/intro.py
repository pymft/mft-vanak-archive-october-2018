import urllib.request

url = "http://www.python.org"

with urllib.request.urlopen(url) as req:
    text = req.read()


print(type(text))
print(text)
