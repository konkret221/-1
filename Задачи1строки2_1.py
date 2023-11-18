def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st

print(shortener('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)'))
print(shortener('(лишнее(лишнее))Падал прошлогодний (лишнее(лишнее(лишнее)))снег'))