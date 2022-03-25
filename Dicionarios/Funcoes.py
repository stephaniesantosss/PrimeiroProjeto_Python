def perguntar():
    return input("O que deseja realizar ?\n" +
                 "<I> - Para inserir usuário\n" +
                 "<P> - Para pesquisar usuário\n" +
                 "<E> - Pra excluir usuário\n" +
                 "<L> - Para listar usuário: ").upper()


def inserir(dicionario):
    dicionario[
        input("Digite o login: ").upper()] = [
        input("Digite o nome: ").upper(),
        input("Digite a ultima data de acesso: ").upper(),
        input("Qual ultima estação acessada: ").upper()
    ]

    salvar(dicionario)


def salvar(dicionario):
    with open("../Manipulacao_Arquivos/bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
