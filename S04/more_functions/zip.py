lst1 = [1, 2, 3, 4, 5]
lst2 = [10, 20, 30, 40, 50]
lst_zip = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
print(lst_zip)

out = zip(lst1, lst2)
print(list(out))

for x, y in zip(lst1, lst2):
    print(x, y)