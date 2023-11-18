from collections import Counter

def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])

print(top3('Улыбкой ясною природа Сквозь сон встречает утро года Синея блещут небеса. Еще прозрачные, леса'))
print(top3('АаА'))
print(top3('Голова думала'))