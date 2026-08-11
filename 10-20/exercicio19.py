produto = float(input("Digite o preço do produto: "))
desconto = produto - (produto * 0.15)

if produto > 100:
    print(f"Seu produto com desconto aplicado é {desconto}")
else:
    print("Seu produto não tem os requisitos para ter desconto.")
