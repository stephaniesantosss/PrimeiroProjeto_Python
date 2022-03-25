# basedados = []
#
# with open("iris.data", "r") as arquivo:
#     for registro in arquivo.readlines():
#         basedados.append(registro.split(","))
#
# print(basedados)
#
# print(float(basedados[0][0]) + float(basedados[0][1]))

# lendo um arquivo json ##########################
#
# import json
#
# with open("bd.json", "r") as arquivoJson:
#     dic = json.load(arquivoJson)
#     for chave, dados in dic.items():
#         print(chave + " " + str(dados))

#### criando um arquivo json ################

import json

dicionario = {
    "STEPHANIE": [
        "STEPHANIE SANTOS",
        "14/09/1998",
        "TI"
    ],
    "JHONY": [
        "JHONY SANTOS",
        "22/08/1990",
        "TI"
    ]
}

with open("bd1.json", "w") as arquivoJson:
    json.dump(dicionario, arquivoJson)
