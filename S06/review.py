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

print("my integer%d." % num)
print("my integer%10d." % num)   # right justified
print("my integer%-10d." % num)   # left justified
print("my integer%010d." % num)   # right justified

num2 = 10000000000000000
print("my integer%10d." % num2)   # right justified


#  floats
var = 10.23
print("my integer%f." % var)
