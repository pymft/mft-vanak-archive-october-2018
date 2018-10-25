f = open('input.txt', mode='r', encoding='utf-8')

text = f.read(6)
print(type(text))
print(text)
text = f.read()
print(text)
# while True:
#     text = f.read(6)
#     if not text:
#         break
#     print(text)
f.close()