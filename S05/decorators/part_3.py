def decorate(f):
    def inner(*args, **kwargs):
        out = f(*args, **kwargs)
        out = "*" + out + "*"
        return out
    return inner


@decorate    # echo = decorate(echo)
def echo(s):
    return s


print(echo("hi"))
# echo = decorate(echo)
# print(echo("hi"))