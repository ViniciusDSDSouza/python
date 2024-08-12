# Listas
# Tipos de Listas
numeros = [1, 2, 3]
strings = ["Vinicius", "Pedro", "Luiz"]
decimais = [10.8, 15.4, 90.1]
listas = [numeros, strings, decimais]

print(numeros) # [1,2,3]
print(numeros[0]) # 1
print(numeros[1]) # 2
print(numeros[2]) # 3

# Manipulação de Listas
# • Alterar Valor
numeros[0] = 5
print(numeros[0]) # 5

# • Adicionar Valor [.append]
numeros.append(4)
print(numeros) # [5, 2, 3, 4]