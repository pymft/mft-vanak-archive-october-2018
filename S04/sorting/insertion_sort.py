def min_new(lst):
    m = lst[0]
    for value in lst:
        if value < m:
            m = value
    return m


lst = [1, 50, 32, 90, 30, 0, 80, 45]
lst_sorted = []


print(lst_sorted, lst)

while lst:
    m_lst = min_new(lst)
    lst_sorted.append(m_lst)
    lst.remove(m_lst)

print(lst_sorted, lst)