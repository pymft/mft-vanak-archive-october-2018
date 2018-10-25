f = open('output.txt', mode='a')
for i in range(4):
    f.write("{i} hello\n".format(i=i))

f.close()


# f.seek()