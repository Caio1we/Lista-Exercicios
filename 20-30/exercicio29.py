n = int(input("Digite um número: "))
total = 1 

for numero in range(n + 1):
    if numero == 0:
        continue
    total *= numero


print(total)
