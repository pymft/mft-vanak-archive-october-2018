
class FileInstance:
    def __init__(self, fname):
        self.path = fname
        self.f = None


    def __enter__(self):
        self.f = open(self.path, 'w')
        return self

    def add(self, s):
        self.f.write('\n' + s)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()



with FileInstance('./input.txt') as s:
    s.add("hello")

