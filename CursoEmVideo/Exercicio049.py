#49 Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
numero = int(input("Digite um número: "));
print("**************** TABUADA *************")
for c in range(0,10+1):
    print(f'{numero} x {c} = {numero*c}')
print('**************************************')