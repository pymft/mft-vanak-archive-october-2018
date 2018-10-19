def echo(s):
    return s[::-1]

def tag_maker(tag):
    def inner(s):
        out = "<" + tag + ">" + s + "</" + tag + ">"
        return out
    return inner

def decorated(f):
    def inner(s):
        return "****" + f(s) + "****"
    return inner


res = echo("hello")   # hello
print (res)
echo_new = decorated(echo)
res = echo_new("hello")   # <b>hello</b>
print(res)

bold = tag_maker('b')
italic = tag_maker('i')

print(bold("hello"))
print(italic("hello"))