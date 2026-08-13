# 38. Inverta os elementos de uma lista.

lista = ["1", "2", "3", "4"]
listainvertida = []

tamanho = len(lista)

while True:
    if tamanho == 0:
        break
    listainvertida.append(lista[tamanho - 1])
    tamanho -= 1


print(listainvertida)
