#
pat = "{0}*{0}"

for i in range(8):
    text = "*" * i
    print(pat.format(text))

