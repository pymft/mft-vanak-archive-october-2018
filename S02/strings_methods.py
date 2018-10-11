# string instances
# type: str
text1 = "hello"
text2 = "HELLO"

text1.upper()
text2.lower()

for i in range(10):
    line = " " * (2*i+1)
    line = "*" + line + "*"
    line_new = line.center(21)
    print(line_new)

text = "all work and no play makes Jack a dull boy!"
print(text)
text2 = text.replace('Jack', 'Someone Else')
print(text2)