# 23. Peça um número e mostre a tabuada dele.

numeroT = int(input("Digite um número: "))

for numero in range(11):
    print(f"{numeroT} x {numero} = {numeroT * numero}")
