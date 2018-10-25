# regular
text = "x{num}x".format(num=10)
print(text)

# right just
text = "x{num:>30}x".format(num=10)
print(text)

# left just
text = "x{num:<30}x".format(num=10)
print(text)
# center justify
text = "x{num:*^30}x".format(num=10)
print(text)

#  precision
text = "x{num:*^30.2f}x".format(num=10)
print(text)


