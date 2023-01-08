# Необходимо считать любой текстовый файл на вашем ПК (можно создать новый)
# и создать на его основе новый файл, где содержимое будет записано в
# обратном порядке. В конце программы вывести на экран оба файла - старый в
# неизменном виде и новый в обратном порядке.

with open('input.txt', 'r', encoding='utf-8') as f:
    symbols = f.read()[::-1]

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(symbols)

print('Исходный файл:')
with open('input.txt', 'r', encoding='utf-8') as f:
    print(f.read())

print('\n' + 'Итоговый файл:')
with open('output.txt', 'r', encoding='utf-8') as f:
    print(f.read())
