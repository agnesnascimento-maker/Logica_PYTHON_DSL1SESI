#AULA COMPLETA -STRINGS EM PYTHON

# - Criação de strings 
# - strings multilinha
# - Operaçôes com strings
# - imutabilidade 
# - Métodos úteis
# - Formatação de texto 
# -unicode e bytes


# -----------------------------------------------
# 1)CRIAÇÃO DE STRINGS
# ------------------------------------------------
# Strings são textos em python.
#Podem ser criadas usando aspas simples ou duplas

texto1 = "Python"
texto2 = "Curso em python"
texto3 = "Copa 'padrão fifa'"
texto4 = 'Copa "padrão fifa"'

print(texto1,texto2,texto3,texto4)

#Python permite mistuar aspas e duplas,dentro da strings sem precisar escapar caracteres

#--------------------
#2) strings multilinhas
#---------------------
#Usando três aspas ("""ou ''') para criar textos que ocupam várias linhas.

menu ="""\
Uso: programa [OPÇÕES]
- h Exibe ajuda
-U Url do dataser
"""
print(menu)

#Esse formato é muito usado para:
# -menus
#documentação
#textos longos

#-----------------------------
#3) CONCATENAÇÃO AUTOMÁTICA
#-----------------------------
# Quando duas strings aparecem lado a lado, o Python junta automaticamente

texto =("Copa" "2026" "Neymar é show mesmo?" "Talvez")
print(texto)

#--------------------------------
# 4) STRINGS COMO SEQUÊNCIAS
#--------------------------------
# Uma string funciona como uma sequência de cractes, casa caractere possui um índice

st = "maracana"
print("Primeira letra":, st[0])
#só exibir a letra: m

print( "ultima Letra;", st[-1]")

print ("Trecho 1.4:", st[1:4])   

print ("Do inicio até 3;", st[:3])

print ("Do 2 até o fim:", st[2:])

 print ("Tamanho ", len(st))
 



