def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst

print(list_sort([3, 19, 21]))
