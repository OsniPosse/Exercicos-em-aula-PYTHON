


#1.— Considere x <- “C”, y <- “B”, z <- “A”. Indique se cada expressão é V ou F: 
#a) x < y 
#b) y = z 
#c) y <> z 
#d) (x < y) e (y = z) 
#e) (x > y) ou (y = z) 
#f) não (x = “C”)"""

"""x='C'
y='B'
z='A'
print('Indique se cada expressão é V ou F:')
print('x<y',(x<y))
print('y==z',y==z)
print('y!=z',y!=z)
print('x<y and y==z',x<y and y==z)
print('x>y or y==z',x>y or y==z)
print('not x=="C"',not x=='C')"""



#2.— Escreva condições lógicas para: 
#a) verificar se c está no intervalo [“0”, “9”];
"""c=int(input('digite um numero para C:  '))
if c>=0 and c<=9:
   print('C esta no intervalo de 0 e 9')
else:
    print('c não esta no intervalo de 0 e 9')"""


#b) verificar se um caractere c é uma letra minúscula.
"""c=str(input('verificar se um caractere c é uma letra minúscula.'))
if c=='c':
    print('minusculo')
else:
    print('maiusculo')"""


#3.— Escreva um algoritmo que leia um caractere e indique se é ou não um carácter hexadecimal
"""n = input("digite um caracter e descubra se é hexadecimal: ")
if n >= "0" and n <= "9" or n >= "a" and n <= "f" or n >= "A" and n <= "F":
    print("é hexadecimal")
else:
    print("não é hexadecimal")"""

#4. — Ler dois nomes próprios de pessoas e escrevê-los por ordem alfabética
"""name1=str(input('digite um nome:  '))
name2=str(input('digite outro nome: '))
if name1<name2:
    print('em ordem alfabetica:  ',name1,',',name2)
else:
    print('em ordem alfabetica:  ',name2,',',name1)"""

#5. — Pedir ao utilizador para “criar uma nova password” e para repetir a password criada. Dar como 
#resultado, conforme a situação: 
#• Obrigado, a sua password foi criada 
#• As passwords não coincidem

"""var_pass = int(input("digite a senha com 8 caracteres: "))

pass1 = int(input("repita a senha com 8 caracters"))

if var_pass == pass1:
    print("thanks, create password")
else:
    print("error password")"""

#6. — Ler um carácter e classificar, conforme a situação em: 
# É um dígito (decimal) 
# É uma letra minúscula 
# É uma letra maiúscula 
# É um outro sinal ou símbolo """

"""n = input("digite um caracter e descubra se é decimal, maiusculo,minusculo, sinal ou simbolo: ")
if n >= "0" and n <= "9":
    tipo = "decimal"
else:
    if n >= "A" and n <= "Z":
        tipo = "maiusculo"
    else:
        if n >= "a" and n <= "z":
            tipo = "minusculo"
        else:
            tipo = "sinal ou simbolo"
print(tipo)"""
