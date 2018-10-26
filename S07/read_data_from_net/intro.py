import re
import urllib.request

url = ""

with urllib.request.urlopen(url) as req:
    text = req.read()
    text = text.decode('utf-8')


pat = r"\"mailto:(.*)\""
res = re.findall(pat, text)
print(res)
