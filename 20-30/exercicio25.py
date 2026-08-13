# 25. Peça números até o usuário digitar 0 e mostre a soma deles.

numeros = []
numero = 2
soma = 0
while numero != 0:
    numero = int(input("Digite um número: "))
    numeros.append(numero)


for n in numeros:
    if n == 0:
        numeros.remove(0)
    soma += n

print(f"Numeros salvos: {numeros}")

print(f"A soma de todos os números pedidos é {soma}")
