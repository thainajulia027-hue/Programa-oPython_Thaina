import os
os.system('clear')

numero = int(input("Digite um número: "))

if numero %3 == 0 and  numero %7== 0:
    print("O número é divisível por 3 ")
else:
    print("O número é divisível por 7 ")