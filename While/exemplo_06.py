import os
os.system('clear')

cont = 0
acm = 0

numero = int(input("digite um numero ou 0 para encerrar: "))

while True:
    numero = int(input("Digite um número ou 0 para encerrar: "))
    if numero == 0:
        break  
    acm += numero

print(f"Programa encerrado. A soma total foi {acm}.")
