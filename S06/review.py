num = 10
value = 20
# print("number = ", num)
#
# print("number = "+ str(num))
# #     |<------------------>|
# #     |<---------->|
# print("number = %s" % (num))
#
# print("number = %s and value = %s" % (value, range))
# print("number = " + str(value) + " and value = " + str(range))

#  numbers (int) : %d
#
# print("my integer%d." % num)
# print("my integer%10d." % num)   # right justified
# print("my integer%-10d." % num)   # left justified
# print("my integer%010d." % num)   # right justified
#
# num2 = 10000000000000000
# print("my integer%10d." % num2)   # right justified
#

# #  floats
# var = 10.27
# print("my integer%fx" % var)        # my integer10.270000x
# print("my integer%20fx" % var)     # my integer           10.270000x
# print("my integer%-20fx" % var)     # my integer10.2700             x
# print("my integer%-20.4fx" % var)   # my integer10.2700             x
# print("my integer%20.1fx" % var)    # my integer                10.3x

#  scientific numbers
var = 0.00000000000345345
print("my integer %ex" % var)
print("my integer %20ex" % var)
print("my integer %-20ex" % var)
print("my integer %-20.4ex" % var)
print("my integer %20.1ex" % var)

