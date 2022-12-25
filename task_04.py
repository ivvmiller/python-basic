# Есть словарь dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
# Составить из него новый словарь, содержащий только те элементы, у которых значение
# больше или равно 3.

dct = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dct = {}
for k in dct.keys():
    if dct[k] >= 3:
        new_dct[k] = dct[k]

print('Старый словарь: ', dct)
print('Новый словарь:', new_dct)
