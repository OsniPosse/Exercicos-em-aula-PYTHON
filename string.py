#print caracteres com for e while (usar len())
i=0
c='python'
while i<len(c):
    print(c[i])
    i+=1

#print caracteres com 'for in range'
'''
c='python'
for i in range (len(c)):
    print(c[i])
'''

#contar caracteres com for sem len()
'''c='python'
for i in c:
    print(i)'''

#funçao para contar as vezes que determinado caracter aparece numa string
'''def conta(l,p):
    contador=0
    for i in p:
        if i==l:
            contador+=1
    return contador
p=str(input('palavra: '))
l=str(input('letra: '))
print('a letra repete:',conta(l,p),'vezes')'''
    
#validar se dominio é registado em Portugal(.pt)
'''
dominio=str(input('digite um dominio'))
if '.pt'== dominio[-3:]:
    print('dominio valido')
else:
    print('dominio invalido')
'''
'''dominio=input('digite o dominio')
while  dominio[-3:]!='.pt':
    print('dominio invalido')
    dominio=input('digite o dominio')
print('dominio valido')'''

#sites seguros(sim/não)
'''site=str(input('digite o site:  '))
if site[:8]== 'https://':
    print('site seguro ')
else:
    print('site inseguro ')'''

'''site=input('digite o site:  ')
while site[:5]!='https':
    print('site inseguro')
    site=input('digite o site:  ')
print('site seguro')'''

#validar num de telefone 
'''n=str(input('digite um numero de telefone'))
prefixo= ('91','92','93','96','21','22' )
if len(n)==9 and n[:2]in prefixo:
    print('numero valido')
else:
    print('numero invalido')'''


#validar email formaçao @formacao.iefp.pt e antes do @ tem que ser digitos
'''def valid_email(email):
    
    if '@formacao.iefp.pt' != email[-17:]:
        return False
    
   
    username = email[:-17] 
    
   
    if len(username) == 0:
         return False
    
   
    for i in username:
        if not i.isdigit():
            return False
    
    return True
        
  
email=str(input('digite o email  '))
print(valid_email(email))'''


#verificar palindromo (palavras iguais de tras pra frente de frente pra tras)
'''def palindromo(texto):
    
    return texto == texto[::-1]
texto=str(input('digite uma palavra para verificar se é um palindromo'))
print(palindromo(texto))  '''    
  
#transformar string em inteiro, usando int() para cada caracter mas não para o numero
'''def StrforInt(texto):
    multiplicador=1
    soma=0
    for i in texto[::-1]:    
        inteiro=int(i)
        c=inteiro*multiplicador
        soma=soma+c
        multiplicador=multiplicador*10
    print(type(soma))
    return soma
        

texto=str(input('digite um numero'))
print(StrforInt(texto))'''    


'''texto = "12345"
inteiros = [int(char) for char in texto]

print(inteiros) '''

#transformar int em str, sem usar str()
'''def intTostr(n):
    soma=""
    for i in range(len(n)):
        texto= chr(i+ord("1"))
        soma=soma+texto
        print(type(texto))
        
    return soma

n=input('digite um numero')
print(intTostr(n))'''

'''numero = 789
texto = "%d" % numero'''

#BinToDec
'''def bintodec(str):
    soma=0
    p=0
    for i in str[::-1]:
        inteiro=int(i)
        soma=soma+(inteiro*2**p)
        p=p+1
    return soma

str=input("digite um binario")
print(bintodec(str))'''
        


'''binario = "1010"
decimal = int(binario, 2)
print(decimal) '''

#DecToBin

'''def dectobin(quociente):
    container=""
    while quociente>0:
        quociente=quociente//2
        resto=quociente%2 
        container=container+str(resto)
    return container

n=int(input('digite um decimal'))
print(type(str))
print(dectobin(n))'''


'''decimal = 10
binario = bin(decimal)
print(binario) 

apenas_bits = bin(decimal)[2:] '''


#Codificar/descodificar um texto, com cifra Cifra de Cesar

'''def criptografia(f,i):
    soma=""
    for c in f:
        if c==" ":
            soma=soma+c
        else:
            cascii=ord(c)
            cascii=cascii-i # para codificar casii=cascii+i 
            c=chr(cascii)
            soma=soma+c
        
    return soma

frase=str(input('digite uma frase para criptografar:  '))
incremento=int(input('digite por quantos quer somar os caracteres da frase:  '))
print(criptografia(frase,incremento))  '''  




'''#validação de ISBN
def validacao(isbn):
    contador=0

    if len(isbn)!=13:
        return False
    for i in isbn:
        soma=isbn[::-1] + isbn[-1::]       
        if soma%10!=0:
            return False
        
        
    return True    

isbn=(input('digite o isbn com 13 digitos'))
print(validacao(isbn))
'''


#exercicio treinamento
'''s='abcd'
c='f'
for i in s:
    if i==c:
        print('a letra',c,'esta em', s)
        break
    else:   
        print('a letra',c ,'não esta em', s)
        break'''




# treinamento
'''palavra='programacao'
contador=0
for i in palavra:
    if 'a'==i:
        contador+=1
print(contador)  '''

'''palavra="P1y2t3h4o5n"
for letra in palavra:
    if letra.isalpha():
        print(letra, end="") '''       

'''senha=str(input('digite uma senha de 6 digitos e com uma letra "a":'))
while len(senha)!=6 or 'a' not in senha.lower():
    print('erro, senha deve conter 6 digitos')
    senha=input('digite uma senha de 6 digitos:')
print('senha salva')'''
        


'''nome='python'
for i in range (len(nome)+1):
    print(nome[:i])'''

