##Exercícios - Estruturas iterativas - ciclos 
##Ciclo “While do/Enquanto” 
 
'''exemplo while
n=0
while(n<=9):
    print(n)
    n=n+1
exemplo soma
soma=0
n=0
while (n<=9):
    soma=soma+n
    n=n+1
print (soma)'''

##1. Escrever os números inteiros ímpares entre 1 e n (inserido pelo utilizador)
'''n=int(input('digite um numero'))
impar=1
while impar<=n:
    print(impar)
    impar=impar+2'''
    
##2. Somar os números pares entre 0 e n (inserido pelo utilizador).
'''n=int(input('digite um numero'))
par=0
while par<=n:
    print(par)
    par=par+2'''

##3. Escrever a tabuada de um número n (inserido pelo utilizador, entre 1 e 9)
'''numero=int(input('digite um numero para ter sua tabuada'))
tab=0
n=0
while n<10:
    tab=tab+numero
    n=n+1
    print(numero,'X',n,'=',tab)'''
    
      
##4. Escrever todos os números inteiros entre um número n e um número m (em que n < m)

'''n=int(input('digite um numero'))
m=int(input('digite outro numero maior que o primeiro'))
        
while(n<=m):
    print(n)
    n=n+1'''

##5. Somar todos os números inteiros entre um número n e um número m (em que n < m)

'''n=int(input('digite um numero'))
m=int(input('digite outro numero maior que o primeiro'))
soma=0
while (n<=m):
    soma=soma+n
    n=n+1
print (soma)'''

##6. Calcular (e escrever) o fatorial de um número n (inserido pelo utilizador, entre 0 e 10)

'''n=int(input('digite um numero entre 0 e 10: '))
i=n
fat=1
while i>1:
    fat=fat*i
    i=i-1
print('o fatorial de  ',n,'é',fat)'''


    
    
