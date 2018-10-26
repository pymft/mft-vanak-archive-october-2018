import re
from urllib.request import urlopen


def get_urls(url):
    pat = r'href=[\'"]?(https?://[^\'" >]+)'
    with urlopen(url) as f:
        text = f.read().decode('utf-8')

    result = re.findall(pat, text)
    return result


res = get_urls("http://www.python.org")
for r in res:
    print("\033[35;0mgetting links from : {r}\033[0m".format(r=r))
    try:
        r_res = get_urls(r)
    except:
        print("\033[31;0mSomething went wrong with {r}\033[0m".format(r=r))
    print(r_res)

