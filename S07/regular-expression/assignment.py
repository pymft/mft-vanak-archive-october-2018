import re


f = open('text', 'r')
text = f.read()
f.close()

pat = r".*O\s+(.*)!.*O\s+(.*)!,? Keep"
res = re.findall(pat, text)

for i, word in enumerate(res):
    print(i, word)
