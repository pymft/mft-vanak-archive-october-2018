import re
from urllib.request import urlopen


def get_urls(url):
    pat = r'href=[\'"]?https?://([^\'" >]+)'
    with urlopen(url) as f:
        text = f.read().decode('utf-8')

    result = re.findall(pat, text)
    return result


res = get_urls("http://www.python.org")
print(res)