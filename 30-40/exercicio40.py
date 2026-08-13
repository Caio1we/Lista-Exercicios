# 40. Ordene uma lista em ordem crescente.

lista = [42, 7, 19, 3, 88, 15, 23, 4, 91, 10]


tamanho = len(lista)

for e in range(tamanho):
    for i in range(0, tamanho-e-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]


print(lista)
