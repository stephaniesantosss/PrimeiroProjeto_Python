inventario = []
resposta = "S"

while resposta == "S":
    # append adiciona o valor a lista
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Numero Serial: ")))
    inventario.append(input("Departamento: "))
    # \"S\" é para mostrar o s com aspas e não seu valor
    resposta = input("Digite \"S\" para continuar: ").upper()

# para cada elemento no inventario execute:
for elemento in inventario:
    print(elemento)
