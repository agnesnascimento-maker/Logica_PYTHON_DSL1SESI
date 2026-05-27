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
print( "Primeira letra":, st[0]")
#só exibir a letra: m

print( "ultima Letra;", st[-1]")

print ("Trecho 1.4:", st[1:4])   

print ("Do inicio até 3;", st[:3])

print ("Do 2 até o fim:", st[2:])

 print ("Tamanho ", len(st))

 #-----------------------------------------
 # 5) OPERAÇOES COM STRINGS
 #-----------------------------------------
 # Python permite várias operações com strings

 print ("m" in st)
 # Significa que a letra "m" existe dentro da  string

 print("x" not in st)
 # Significa que "X" não existe na string

 print("m" + "aracana" + texto1)
 #Operador +concatena strings 

 #--------------------------------
 # 6) STRINGS SÃO IMUTÁVEIS
#---------------------------------------
# Strings não podem ser alteradas diretamente !!!
# Isso significa que o conteúdo original não muda.
# o que acontece é a criação de uma nova string.

texto = "python 3"

# Método replace cria uma nova string
texto = texto.replace("3", "2")

print(texto)

#---------------------
# 7 MÉTODOS IMPORTANTES 
#----------------------
#Strings possuem vários métodos úteis.

cidade= "maracana"
#Coloca a primeira letra em maiúscula.
print(cidade.capitalize())

#conta quantas vezes "a" aparece
print(cidade.count("a"))

# Verificar se começa com "m"
print (cidade.startswith("m"))

# Verificar se começa com "m"
print (cidade.endswith("z"))

frase ="copa de 2002"

#divide a string em uma lista
print(frase.split(" "))

# -------------------------------------
# 8) FORMATAÇÃO DE STRINGS 
# -------------------------------------