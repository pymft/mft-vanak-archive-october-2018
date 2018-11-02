import urllib.request


class Brower:
    instances = []
    read_instances = []

    def __init__(self, url):
        self.url = url
        self.__text = ''
        # FIXME : do not allow to instantiate duplicated url

    @property
    def text(self):
        if not self.__text:
            # send request and blaah blaah
            pass
        return self.__text

    def save(self, name=None):
        """
        :param str name: path to save html file
        :return:
        """
        # use `open` function, mode `w`

        # fixme: use with ,
        if name is None:
            pass
            # how to find site's title via urllib.request
        with open(name, 'w') as f:
            f.write(self.text)

    def get_links(self):
        """
        :return: list of Browsers
        """
        pass


if __name__ == '__main__':
    b1 = Brower('https://www.python.org')
    b1.save('./python.html')
