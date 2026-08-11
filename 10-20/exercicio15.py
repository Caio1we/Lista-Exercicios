numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maiorNumero = numero1

if numero2 > maiorNumero:
    maiorNumero = numero2

if numero3 > maiorNumero:
    maiorNumero = numero3

print(f"O maior número é {maiorNumero}")
