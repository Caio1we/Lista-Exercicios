# 36. Conte quantos números pares existem na lista.

lista = [2, 6,8,3,7,17,9,20]
pares = 0

for e in lista:
    if e % 2 == 0:
        pares += 1


print(f"Existem {pares} pares ")
