#
pat = "{s:>{h}}*{s:<{h}}"

h = 30
for i in range(h+1):
    text = "*" * i
    print(pat.format(s=text, h=h))

