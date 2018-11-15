# Load

with open('values.txt', 'r') as f:
    text = f.read()

dct = eval(text)
print(dct, type(dct))