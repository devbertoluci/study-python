# Declaração de uma lista

minha_lista = [1, 2, 3, 4, 5]

# Exibindo a lista
print(minha_lista)

# Exibindo os elementos da lista
minha_lista[0] = "Python"
print(minha_lista[5])
print(minha_lista[6])
print(minha_lista[0:9])
print(minha_lista[:10])
print(minha_lista[5:])

#  -------------------------------- Metodos de listas --------------------------------

# Metodo append
minha_lista.append("!") # Adiciona um elemento ao final da lista
print(minha_lista)

# Metodo Index
indice = minha_lista.index("Python") # Retorna o indice do elemento
print(indice)

# Metodo Insert
minha_lista.insert(2, 10) # Adiciona um elemento em uma posição especifica
print(minha_lista)

# Metodo Pop
minha_lista.pop(1) # Remove um elemento especifico
print(minha_lista)

# Metodo Remove
minha_lista.remove("Python") # Remove um elemento especifico
print(minha_lista)

# Metodo Sort
minha_lista.sort() # Ordena a lista
print(minha_lista)

# Metodo Reverse
minha_lista.reverse() # Inverte a ordem dos elementos
print(minha_lista)
