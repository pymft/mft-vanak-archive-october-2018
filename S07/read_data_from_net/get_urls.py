import re
from urllib.request import urlopen
import urllib.error


def get_urls(url):
    pat = r'href=[\'"]?(https?://[^\'" >]+)'
    with urlopen(url) as f:
        text = f.read().decode('utf-8')

    result = re.findall(pat, text)
    return result


res = get_urls("http://www.python.org")
for r in res:
    print("getting links from : {r}".format(r=r))
    try:
        r_res = get_urls(r)
    except urllib.error.URLError:
        print("URL ERROR")
        continue

    print (r_res)