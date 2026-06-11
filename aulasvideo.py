##for c in range(10,0):
##    print(c)
##print("fim")
##c=1
##while c<10:
##    print(c)
##    c+=1
##print(c)    

'''n=1
par=impar=0
while n!=0:
    n=int(input("digite"))
    if n%2==0:
        par+=1
        n==par
    else:
        impar+=1
print("par{} ou impar{}".format(par,impar))'''  


def fat(n):
    fat=1
    for i in range(1,n-1):
        fat*=i
    return fat    
n=int(input("digite"))
print(fat(n))

'''def primo(n):
    
    if n<2:
        return "invalido"
        
    for i in range(2,n+1):
        primo=True
        for i2 in range(2,i):
            if i%i2==0:
                primo= False
                break
        if primo==True:
            print(i)
    return "ciclo finalizado"        
            

n=int(input("digite"))
print(primo(n) )
'''





## [Base] Defina a função fatorial 
##o fact_r (n) 
##o >>> fact (6) 
##o 720

'''def fat(n):
    i=1
    fat=1
    while n>=i:
        fat=fat*i
        i=i+1
    return fat

num=int(input("digite: "))
print(fat(num))'''


## [Base] Defina uma função que some todos os números de 1 até n 
##o soma_n (n) 
##o >>> soma_n (6) 
##o 11
'''def soma(n):
    soma=0
    for i in range(1,n): -- n+1 para somar o n
        soma+=i
    return soma 
    
num=int(input("digite: "))
print(soma(num))'''

## [Intermédio] Defina uma função que conte todos os elementos de uma lista 
##o conta_elem (l) 
##o >>> conta_elem ([1,2,3])
##o 3

'''def lista(lst):
    return len(lst)

num=[1,2,3,4]
print(lista(num))'''

## [Intermédio] Defina uma função que some todos os elementos de uma lista 
##o soma_elem (l) 
##o >>> soma_elem ([1,2,3]) 
##o 6
'''def somalst(lista):
    soma=0
    for i in range(len(lista)+1):
        soma+=i
    return soma    


lst=[1,2,3,4]
print(somalst(lst))'''
## [Intermédio] Defina a função multiplicação de forma recursiva 
##o mult_r (m1,m2) 
##o >>> mult_r (8,7) 
##o 56 
## [Intermédio] Defina a função exponenciação de forma recursiva 
##o exp_r (b,e) 
##o >>> exp (2,5) 
##o 32 
## [Intermédio+] Defina uma função que reverta uma string 
##o reverse_s (s) 
##o >>> reverse_s (‘pyhton’) 
##o ‘nothyp’ 
## [Intermédio+] Defina uma função que conte as vogais de uma string 
##o conta_vogais(s) 
##o >>> conta_vogais (‘python’) 
##o 1

