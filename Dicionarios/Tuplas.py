usuarios = {}
emails = ["stephanieps2016@hotmail.com", "stephanie@gmail.com"]

tupla = list(enumerate(emails))

for chave in range(0, len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("digite o nome: "), input("Digite o nível: ")]

for chave, dado in usuarios.items():
    print("Usuario...:", chave[0])
    print("Email...:", chave[1])
    print("Nome...:", dado[0])
    print("Nivel...:", dado[1])
