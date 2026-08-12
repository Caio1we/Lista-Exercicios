pares = []

for n in range(51):
    if n == 0:
        continue
    if n % 2 == 0:
        pares.append(n)

print(f"Existem {len(pares)} numeros pares de 1 a 50")

