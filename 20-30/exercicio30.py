# 30. Peça um número ao usuário e mostre a soma de todos os números de 1 até esse número.

total = 0 

n = int(input("Digite um número: "))

for numero in range(n + 1):
    total += numero
print(total)
