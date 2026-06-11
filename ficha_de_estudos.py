## [Base] Construir lista com ciclo “for”. Ler 5 números naturais e inserir numa lista
# 1. Inicializar uma lista vazia
'''numeros = []
n=1,2,3,4,5
for i in n :
    numeros=numeros+[i]
print("Lista de números:", numeros)'''

## [Base] Construir lista com “range”. Criar uma lista com os números inteiros até 20
'''lst=[]
for i in range(20):
    i=i+1
    lst=lst+[i]
print(lst)'''
## [Base] Construir lista com “range”. Criar uma lista com os números pares até 20
'''lst=[]
for i in range(20):
    i+=1
    if i %2==0:
        lst=lst+[i]
print(lst)'''
## [Base] Definir uma ‘script’ que faça print de todos os elementos de uma lista.
'''lista=[1,2,3,4,5,6]
print(lista)'''
## [Base] Definir uma função que conte todos os elementos de uma lista 
##o conta_elem (l) 
##o >>> conta_elem ([1,2,3]) 
##o 3
'''def cont_elem(lista):
    cont=0
    for i in lista:
        cont=cont+1
    return  cont
lista=[1,2,3]
print(cont_elem(lista))'''
## [Base] Definir uma função que some todos os elementos de uma lista e calcule a média. 
##o soma_elem (l) 
##o >>> soma_elem ([1,2,3]) 
##o 6
'''def soma_elem(l):
    soma=0
    for i in l:
        soma=soma+i
    return soma    
l=[1,2,3]
print(soma_elem(l))'''
    

##Guia Prático 
##o  
## [Intermédio] Definir uma função que retorne o maior e menor de todos os elementos de uma lista. 
##o soma_elem (l) 
##o >>> soma_elem ([1,2,3]) 
##o Maior: 3, menor: 1
'''def soma_elem(l):
    for i in l:
        maior=l[0]
        menor=l[0]
        if i>maior:
            maior=i
            
        if i<menor:
            menor=i
    return maior,menor
        
        
       
lista=[1,2,3]
print(soma_elem(lista))'''
        
            
## [Intermédio] Definir uma função que retorne uma lista com todos os divisores de um número n por 
##ordem crescente. 
##o lista_div (12) 
##o >>> [1,2,3,4,6,12]

'''def lista_div(n):
    div=[]
    for i in range(1,n+1):
        if n%i==0:
            div=div+[i]
    return div
        
n=12
print(lista_div(n))'''
         

## [Intermédio] Definir uma função que retorne uma lista com todos os números primos até um nú
##mero ‘n’. 
##o primos (20) 
##o >>> [1,2,3,5,7,11,13,17,19]
'''def primos(n):
    if n<2:
        return False
    for i in range(2,n+1):
        primo=True
        for i2 in range(2,i):
            if i%i2==0:
                primo=False
                break
        if primo==True:
            print(i)
    return 'ciclo finalizado'
n=20
print(primos(n))  ''' 
    
    
## [Intermédio] Definir uma função que procura um elemento numa lista e retorna o índice onde se 
##encontra
'''def search_element(lista,elem):
    for i in range(len(lista)):
        if lista[i]==elem:
            return i
    return 'não existe'
        
        
l=[10, 20, 30, 40, 50]
e=30
print(search_element(l,e))'''



## [Intermédio] Definir uma função que ordena de forma crescente uma lista de números naturais.
'''def ordenar_lista(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    return lista

lista = [12, 1, 5, 3, 20]
print(ordenar_lista(lista))'''


