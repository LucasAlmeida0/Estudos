expressão = str(input('Digite uma expressão: '))
total = expressão.count(')') + expressão.count('(') 


if total % 2  == 0:
    print('Sua expressão está correta')
else:
    print('Sua expressão está incorreta')