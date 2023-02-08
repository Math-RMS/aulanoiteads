# 1
n1 = float(input("Insira a sua primeira nota: "))
n2 = float(input("Insira a sua segunda nota: "))
n3 = float(input("Insira a sua terceira nota: "))
me = ((n1+n2+n3)/3)

print("A média de aproveitamento de tal aluno é: ", ((n1+n2*2+n3*3+me)/7))
if(me>=9):
    print("A média é maior ou igual a 9 :) ")
if(me<4):
    print("A média é menor que 4 :( ")
else:
    print("A média está OK :|")

#2
nome = str(input("Insira o seu nome completo: "))
ende = str(input("Insira o seu endereço: "))
cep = int(input("Insira o seu CEP: "))
tel = int(input("Insira o seu telefone: "))

print("Seu nome:", (nome))
print("Seu endereço:", (ende))
print("Seu cep:", (cep), "Seu telefone:", (tel))

# 3
print("XXXXX")
print("X   X")
print("X   X")
print("X   X")
print("XXXXX")

# 4
nome = str(input("Insira o nome do aluno: "))
nota = str(input("Insira a nota do aluno: "))

print("ALUNO(A)      NOTA")
print("========    ========")
print((nome),"     ",(nota))

# 5
print("FIM - 0\n1 - INCLUI\n2 - Altera\n3 - EXCLUI\n4 - CONSULTA ")
us = int(input("Insira uma das opções: "))

if(us==0):
    print("FIM")
if(us==1):
    print("INCLUI")
if(us==2):
    print("ALTERA")
if(us==3):
    print("EXCLUI")
if(us==4):
    print("CONSULTA")
else:
    print("Item não encontrado. ")


# 6
x = int(input("Insira um numero: "))

print(" " " " " " " " " " " " " "" "" "" "" " " " " ", (x),)
print(" " " " " " " " " " " " " " " " " " " " " ", (x), (x), (x),)
print(" " " " " " " " " " " " " " " " " ", (x), (x), (x), (x), (x),)
print(" " " " " " " " " "" "" ", (x), (x), (x), (x), (x), (x), (x),)
print(" "" " " " " "" ", (x), (x), (x), (x), (x), (x), (x), (x), (x),)
print(" ""  ", (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x),)
print(" ", (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x),) 
print((x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x), (x)) 
print("             ", (x), (x),"      ") 
print("             ", (x), (x),"      ") 
print("           ", (x), (x), (x), (x),"     ")

# 7
x = int(17)
y = float(3.2)

print (x/4+y)
print (x*y**6)
# print (x%4), ((y*10)//4)
print ((x/6//x/3)+4)


#8
n = float(input("Insira o numero de termos: "))
a1 = float(input("Insira o valor inicial: "))
an = float(input("Insira o valor final: "))
s = n*(a1+an)/2
print ("O resultado das somas desta PA é: ", (s))

# 9
a1 = float(input("Insira o valor inicial: "))
n = float(input("Insira a quantidade de termos: "))
q = float(input("Insira a razão: "))

if(q<2):
    print ("A razão deve ser maior ou igual a dois :(")
else:
    print ("O resultado desta PA é: ", (a1*(q**n -1)/(q-1)))

# 10
ano = int(input("Insira o seu ano de nascimento: "))
vota = (ano-2023)*-1

if(vota<16):
    print ("Você não podera votar esse ano, aguarde mais tempo")
else:
    print ("Você podera votar esse ano, pense bem antes de votar")

# 11
senha = int(input("Insira a sua senha: "))
certa = 8765

if(senha==certa):
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")

# 12
altura = float(input("Insira a sua altura: "))
print ("Digite '1' se for do sexo masculino ou digite '2' se for do sexo femenino")
sexo = int(input("Insira o digito do seu sexo: "))

if(sexo==1):
    print("O seu peso ideal seria: ", (72.7*altura)-58)
if(sexo==2):
    print("O seu peso ideal seria: ", (62.1*altura)-44.7)
else:
    print("Insira novamente o digito que pertense ao seu genero")

# 13 e 14
n = int(input("Insira a quantidade de lados que seu poligono possui: "))

if(n<3):
    print("NÃO É UM\nPOLÍGONO.")
if(n>5):
    print("POLÍGONO NÃO\nIDENTIFICADO")
if(n==3):
    print ("Este polígono é um TRIÂNGULO")
    b = (int(input("Insira a base deste triângulo: ")))
    h = (int(input("Insira a altura deste triângulo: ")))
    print("A área deste triângulo é: ", (b*h/2))
if(n==4):
    print ("Este polígono é um QUADRADO")
    l1 = (int(input("Insira o valor do lado deste quadrado: ")))
    print("A área deste quadrado é: ", (l1*l1))
if(n==5):
    print ("Este polígono é um PENTÁGONO")