name1 = input('введите число: ') # comment
name2 = input('что сделать? ')
name3 = input('введите второе число: ')
print('{} {} {} = '.format(name1 , name2 , name3))
if name2 == '+':
    res = float(name1) + float(name3)
if name2 == '-':
    res = float(name1) - float(name3)
if name2 == '/':
    if name2 != '0':
        res = float(name1) / float(name3)
if name2 == '*':
    res = float(name1) * float(name3)
print(f"Промежуточный результат: {res}")
name2 = input('что сделать? ')
while name2 != '=':
    name3 = input('введите второе число: ')
    if name2 == '+':
        res = res + float(name3)
    if name2 == '-':
        res = res - float(name3)
    if name2 == '/':
        if name2 != '0':
            exit('на ноль не делят')
    if name2 == '*':
        res = res * float(name3)
    print(f"Промежуточный результат: {res}")
print(f"Результат: {res}")
