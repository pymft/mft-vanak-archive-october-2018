import urllib.request


class Brower:
    instances = []
    read_instances = []

    def __init__(self, url):
        self.url = url

    def read(self):
        """reads the site content """
        # we're gonna use `urllib.request` here
        pass

    def save(self, name):
        """
        :param str name: path to save html file
        :return:
        """
        # use `open` function, mode `w`
        pass

    def get_links(self):
        """
        :return: list of Browsers
        """
        pass


if __name__ == '__main__':
    b1 = Brower('https://www.google.com')