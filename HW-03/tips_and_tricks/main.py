def red(f):
    def inner(s):
        return "\033[31;1m" + f(s) + "\033[0m"
    return inner

def blue(f):
    def inner(s):
        return "\033[34;1m" + f(s) + "\033[0m"
    return inner


@blue
def echo(s):
    return s


print(echo("All work and no play makes jack a dull boy"))

