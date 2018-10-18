lst = [1, 2, 3, 4, 5, 6, 7, 8]
is_even = lambda x: x % 2 == 0

out = [x**2 for x in lst if is_even(x)]
filtered_lst = filter(is_even, lst)

# for x in filtered_lst:
#     print(x)

filtered_lst_convert = list(filtered_lst)
print(filtered_lst_convert)