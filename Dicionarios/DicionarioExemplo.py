# Dicionario
usuarios = {}
print(usuarios)

usuarios = {
    "stephanie": ["Stephanie Santos", "23/02/2022", "Recp_01"],
    "jhony": ["Jhony Santos", "27/02/2022", "RaioX_03"]}

print(usuarios)

usuarios["Belinha"] = ["Belinha Santos", "22/02/2022", "RaioX"]
print(usuarios)

print("####----####")
print(usuarios.get("jhony"))
