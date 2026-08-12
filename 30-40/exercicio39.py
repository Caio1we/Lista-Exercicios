lista = [4,6,7,8,3,2,6,9,333,5]

numeroprocurado = 8
achou = False
index = 0

for n in lista:
    if n == numeroprocurado:
        achou = True
        print(f"O número foi achado, index {index}")
        exit(0)
    index += 1

