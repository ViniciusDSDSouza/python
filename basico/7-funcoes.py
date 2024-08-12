# Funções [def]

print("DIGITE DOIS VALORES PARA SOMAR")
print("------------------------------")

def soma(a, b):
    return a+b

valor1 = int((input("1° Valor: ")))
valor2 = int((input("2° Valor: ")))

print("Resultado Final: ", valor1, " + ", valor2, " = ", soma(valor1, valor2))