#tdbase- int, float, boll,strings
#td estrutura-tuples,listas
#tdasst.orinetado a objetos-type,class


#stack-pilhas
#lifo-last in first out(ultimo a entar primeiro a sair)
#push-colocar elementos na lista
#pop-tirar elementos da lista(puxa sempre o ultimo elemento da lista)
#o push e pop são funções qual devemos formar ela, para execurtar o comando qdo chamado

def new():
    return[]

def push(e,p):
    p=p+[e]
    return p

def pop(p):
    if p==[]:
        print('erro')
    return p[:-1]

def view(p):
    print(p)
    
def top(p):
     if p==[]:
        print('erro')
     return p[-1]

def isepty(p): #funçao verificar se lista vazia
    return p==[]

#verificar palindromo (palavras iguais de tras pra frente de frente pra tras)
def palindromo(texto):    
    return texto == texto[::-1]
