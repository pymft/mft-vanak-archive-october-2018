import re
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
            with urllib.request.urlopen(self.url) as req:
                self.__text = req.read().decode('utf-8')
        return self.__text



    def save(self, name=None):
        """
        :param str name: path to save html file
        :return:
        """
        if name is None:
            res = re.findall(r'<title>(.*?)</title>', self.text)
            if res:
                name = res[0] + '.html'
        with open(name, 'w') as f:
            f.write(self.text)


    def get_links(self):
        """
        :return: list of Browsers
        """
        pass


if __name__ == '__main__':
    b1 = Brower('https://www.python.org')
    b1.save()
