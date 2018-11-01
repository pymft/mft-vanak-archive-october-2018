class Color:
    colors = {'red': 31, 'blue': 34, 'yellow': 32}
    intensities = {'d': 0, 'u': 4, 'b': 1, 'r': 7}

    def __init__(self, colorname, intensity='d'):
        self.color_code = self.colors[colorname]
        self.intensity_code = self.intensities[intensity]

    def __call__(self, f):
        def inner(*args, **kw):
            s = f(*args, **kw)
            return "\033[{color};{intensity}m{s}\033[0m".format(
                color=self.color_code,
                intensity=self.intensity_code,
                s=s)

        return inner


@Color('blue')
def echo(s):
    return s


print(echo('hello'))