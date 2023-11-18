from collections import Counter
from functools import reduce
dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}


def sum_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) + Counter(b), dicts))

def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))

print(max_dct(dict_1, dict_2))
print(sum_dct(dict_1, dict_4, dict_3))
print(max_dct(dict_1, dict_2, dict_3, dict_4))
print(sum_dct(dict_1, dict_2, dict_3, dict_4))