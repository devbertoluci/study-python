# Declaração
nome_completo = "Arthur Bertoluci"

nome_completo_aspas = """Arthur
Bertoluci"""

nome_completo_quebra = "Arthur \
Bertoluci"

nome = "Arthur"
sobrenome = "Bertoluci"

print("Nome completo (1a forma)", nome_completo)
print("Nome completo (2a forma)" + nome_completo)
print("Nome completo (3a forma)", nome_completo_aspas)
print("Nome completo (4a forma)", nome_completo_quebra)
print("Nome completo (5a forma)" + "Arthur" + "Bertoluci")
print("Nome completo (6a forma)" + "Arthur", "Bertoluci")
print("Nome completo (7a forma) %s" % nome_completo)
print("Nome completp (8a forma) %s %s" % (nome, sobrenome))
print(f"Nome completo (9a forma) {nome} {sobrenome}")
print("Nome completo (10a forma) {} {}".format(nome, sobrenome))
