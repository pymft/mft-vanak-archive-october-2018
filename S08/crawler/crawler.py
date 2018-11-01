class Browser:
    instances = []

    def __init__(self, url):
        self.url = url


site = 'http://www.python.org'
b = Browser(site)

b.open()    # urllib.request.urlopen
b.save()    # open(harchi, 'w')
b.links()   # regex, list of Browser

