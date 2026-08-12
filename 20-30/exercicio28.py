numeros = []
numerospositivos = []
numerosnegativos = []
for n in range(6):
    if n == 0:
        continue
    nd = int(input(f"Digite o {n}º número: "))
    numeros.append(nd)

    
for numero in numeros:
    if numero > 0:
        numerospositivos.append(numero)
    else:
        numerosnegativos.append(numero)


print(f"Existem {len(numerospositivos)} positivos e {len(numerosnegativos)} negativos ")
