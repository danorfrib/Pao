import dados

print ("Você é um pão. Reflita sobre isso e quando terminar, aperte enter.")

input ()

print ("Qual é o nome do seu pão?")

nome_pão = input ()

print ("Qual é o tipo do seu pão?")

for i in range (len(dados.TIPOS_DE_PÃO)):
    print ("{}: {}".format(i + 1, dados.TIPOS_DE_PÃO[i]))

dados.tipo_pão = int (input ()) - 1

print("Você é {}, um {}.".format(
    nome_pão,
    dados.TIPOS_DE_PÃO[dados.tipo_pão]
))
