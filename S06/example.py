#             *
#            **
#           ***
#          ****
#         *****
#        ******
#       *******

n = 30

pat = "%8s"
pat = "%%%ds" % n   # "%ns"
#        ^^

for i in range(n):
    text = "*" * i
    print(pat % text)

