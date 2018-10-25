#             *
#            **
#           ***
#          ****
#         *****
#        ******
#       *******



pat = "%8s*%-8s"

for i in range(8):
    text = "*" * i
    print(pat % (text, text))

