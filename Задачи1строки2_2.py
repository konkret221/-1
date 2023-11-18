def cleaned_str(st):
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop()
        elif symbol != '@':
            clean_lst.append(symbol)
    return ''.join(clean_lst)

print(cleaned_str('гр@оо@лк@оц@ва'))
print(cleaned_str('сварка@@@@@лоб@ну@'))