f = open('out.txt', 'w')

f.close()


# open
# __enter__
# __exit__

with open('out.txt', 'w') as f:
    text = f.read()
