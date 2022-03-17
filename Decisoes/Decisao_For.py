tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número: ", tabuada)

# contador começa no 1, finaliza quando chegar no 11 e incrementa 1 a cada vez que ele passar pelo for
for valor in range(1, 11, 1):
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada * valor)))
