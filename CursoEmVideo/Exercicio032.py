#32 Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime 
print("Digite 0 para analisar o ano atual")
ano = int(input("Que ano quer analisar? "))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é bissexto")
else:
    ano = 2021
    print(f"O ano {ano} não é bissexto")