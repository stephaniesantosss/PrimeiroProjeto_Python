# input sempre recebe valor como string por padrão
nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
# para definir o tipo da variavel será como abaixo
qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))
media_mensalidade = float(input("Digite a média da mensalidade: "))
print("==============================================================")
# para concatenar String usar o +
print(nome + " trabalha na empresa " + empresa)
# para concatenar valor ou metodo usar ,
print("Possui: ", qtde_funcionarios, " funcionarios.")
print("A média da mensalidade é de: " + str(media_mensalidade))
print("==================Verifique os tipos de dados abaixo==================")
print("O tipo da variavel [nome] é: ", type(nome))
print("O tipo da variavel [empresa] é: ", type(empresa))
print("O tipo da variavel [qtde_funcionarios] é: ", type(qtde_funcionarios))
print("O tipo da variavel [media_mensalidade] é: ", type(media_mensalidade))
