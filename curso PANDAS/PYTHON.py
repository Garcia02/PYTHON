#Adicionar Elementos:
#Adiciona um elemento ao final da lista.
lista = [1, 2, 3]
lista.append(4)
print(lista)  # Saída: [1, 2, 3, 4]
#Insere um elemento em uma posição específica.
lista.insert(1,"a")
print(lista)  # Saída: [1, 'a', 2, 3, 4]
#Remover Elementos:
#Remove a primeira ocorrência de um valor específico.
lista.remove(2)
print(lista)  # Saída: [1, 'a', 3, 4]
#Remove um elemento em uma posição específica ou a lista inteira.
del lista[1]
print(lista)  # Saída: [1, 3, 4]
#Remove e retorna o último elemento ou um elemento em uma posição específica.
ultimo = lista.pop()
print(ultimo)  # Saída: 4
print(lista)   # Saída: [1, 3]
#Encontrar Elementos:
#Retorna o índice da primeira ocorrência de um valor.
posicao = lista.index(3)
print(posicao)  # Saída: 1
#Outras Operações Úteis:
#Ordena a lista em ordem crescente.
lista = [3, 1, 4, 2]
lista.sort()
print(lista)  # Saída: [1, 2, 3, 4]
#Inverte a ordem dos elementos na lista.
lista.reverse()
print(lista)  # Saída: [4, 3, 2, 1]
#Retorna o número de vezes que um valor aparece na lista.
ocorrencias = lista.count(4)
print(ocorrencias)  # Saída: 1