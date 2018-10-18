def merge(lst):
    n = len(lst)
    if n < 2:
        return lst

    right = merge(lst[n//2:])
    left = merge(lst[:n//2])

    lst_sorted = []

    while left and right:
        if left[0] <= right[0]:
            val = left.pop(0)
        else:
            val = right.pop(0)
        lst_sorted.append(val)

    lst_sorted = lst_sorted + left + right

    return lst_sorted

lst = [1, 50, 32, 90, 30, 0, 80, 45]
print(lst)

print(merge(lst))