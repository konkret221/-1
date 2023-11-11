lst = [1, 2, 3, 4, 5]
def change(lst):
    start = lst.pop()
    end = lst.pop(0)
    lst.append(end)
    lst.insert(0, start)
    return lst
print(change(lst))