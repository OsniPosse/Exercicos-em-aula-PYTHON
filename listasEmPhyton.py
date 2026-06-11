##lst1=[1,2,3]
##lst2=[[4,5]]
##lst=lst1+lst2
##'a' in lst
##lst=lst+[6]
##del(lst[1]) -- deletar o elemento 1(0,1,) da lista

##dada ua lista de numeros naturais(ex:[1,2,3,4,5,6,7,8,9]):
##    fazer um print de todos os seus elementos(9 no caso exemplo)
##    contar o numeros de elementos(9 no caso exemplo)*
##    somar todos os elementos (45, no caso exemplo)
##    calcular a media dos elementos(5,no caso exemplo).
##    função "lista_div" com os divisores de um numero n
##    funçao lista com numeros primos ate n
##    função procura_elemento em lsta (retorna indice ou -1) proc_elem(x,l)
##    função IsOrd()lst.Retorna True se lista estiver ordenada


##lst=[1,2,3,4,5,6,7,8,9]
##print(len(lst))
##media= sum(lst)/len(lst) #sum soma os elementos que estao dentro dele
##print(media)
#-----------------------------------------------------------
# contar o numeros de elementos(9 no caso exemplo)
'''def cont(n):
    cont=0
    i=0
    for i in lst:
        cont=cont+i
    return cont   '''
#-----------------------------------------------------------
#função "lista_div" com os divisores de um numero n
##def lista_div(n):
##    divisores=[]
##    
##    for i in range (1,n+1):
##        if n%i==0:
##            divisores=divisores+[i]
##            
##            
##    return divisores
##       
##
##numero=int(input("digite um numero para imprimir seus divisores"))
##print(lista_div(numero))

#----------------------------------------------------------------
# funçao lista com numeros primos ate n
##def primo(n):
##    primo=[]
##    for num in range(2,n+1):
##        retorna= True
##        for i in range(2,int(num**0.5)+1):
##            if num%i==0:
##                retorna = False
##        if retorna==True:
##            primo=primo+[num]
##    return(primo)      
##
##numero=int(input("digite "))
##print(primo(numero))

#--------------------------------------------------------------------
#função procura_elemento em lsta (retorna indice ou -1) proc_elem(x,l)
'''def proc_elem(x,l):
    for i in range(len(l)):
        if l[i]==x:
            return i
    return -1

lista=[1,2,3,4,5]
elemento=int(input("digite um numero para procurar na lista"))
print(proc_elem(elemento,lista))
'''

'''
f(n)=n*f(n-1)
5!=5*4!
1!=1*0! 
n!=n*(n-1)!
f(n)=f(n-1)+f(n-2)'''



'''# função fibonacci teoria dos coelhos
def f(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
       
        return f(n-1)+f(n-2)

meses=int(input("digite o numero de meses para calcular a quantidade de coelhos"))
print(f(meses))  '''      

mpg=float(input("digite o MPG"))

kms=1.61
litros=3.79
consumo=litros/(mpg*kms)*100
print("consumo",consumo)


