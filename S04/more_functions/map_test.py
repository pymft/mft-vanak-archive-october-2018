f = lambda x: x**2

lst = [1, 2, 3, 4, 5]

lst_mapped = []

for i in lst:
    lst_mapped.append(f(i))

print (lst_mapped)

# list comprehension
# {x**2 | x \in lst}
lst_new = [f(x) for x in lst]

lst_new_map = list(map(f, lst))
print(lst_new_map)

print (lst_new )