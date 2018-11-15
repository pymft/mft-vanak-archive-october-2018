#  Dump

dct = {
    'firstname': 'John',
    'lastname': 'Smith'
}


with open('values.txt', 'w') as f:
    text = str(dct)
    f.write(text)