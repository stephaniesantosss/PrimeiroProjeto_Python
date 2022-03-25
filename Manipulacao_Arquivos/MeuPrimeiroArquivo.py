# com o with você nao precisa se preocupar em dar o close no arquivo, ele mesmo finaliza apos conclusão do bloco
# com o W ele cria um novo arquivo
# com o A ele escreve uma nova linha
# o R traz todo o conteudo do arquivo
# with open("primeiro_arquivo.txt", "a") as arquivo:
#    arquivo.write("\nShoooow")

with open("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(linha)
