# 19. Leia o preço de um produto e aplique desconto de 5% se for maior que 100.

produto = float(input("Digite o preço do produto: "))
desconto = produto - (produto * 0.15)

if produto > 100:
    print(f"Seu produto com desconto aplicado é {desconto}")
else:
    print("Seu produto não tem os requisitos para ter desconto.")
