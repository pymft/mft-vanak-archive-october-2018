import re

pat = "[^abcd]"
pat = ""

pat = r"\b([^aeiou])(\w+)\b"
text = "nothing can ever happen twice"

res = re.findall(pat, text)

print(res)