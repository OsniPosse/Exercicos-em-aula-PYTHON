'''class conta:
    num_conta=0 #auto incrmenta numero da conta
    def __init__(self,saldo):
        self.saldo=saldo
        conta.num_conta+=1
        self.conta_num=conta.num_conta

if __name__=="__main__":
    
    conta_01=conta(10000)
    print("saldo: ",conta_01.saldo,"numero conta:",conta_01.conta_num)
'''

'''class Fila:
    def __init__(self):
        self.itens=[]

    def insere(self,elemento):
        self.itens=self.itens+[elemento]
        return self.itens

    def __str__(self):
        s='<'
        for e in self.itens:
            s=s+str(e)+'<'
        return s

    def __len__(self):
        c=0
        for e in self.itens:
            c=c+1
        return c     

fila_prior=Fila()   
fila_prior.insere(1)


print("fila de prioridade",fila_prior)
print ("comprimento da fila",len(fila_prior))'''

def mdc(n,m):
    if m==0:
        return n
    return mdc(m,n%m)
    
def mmc(n,m):
        return abs(n*m)/mdc(n,m)
    
class fracao:
    def __init__(self,numerador,denominador):
        
        self.num=numerador
        self.den=denominador

    def __str__(self):
        
        s=str(self.num)+'/'+str(self.den)
        return s

    def mult(self,outra):
        n=self.num*outra.num
        d=self.den*outra.den
        return fracao(n,d)
# outra forma
class fracao:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador  

    def __str__(self):
        s=str(self.numerador)+"/"+ str(self.denominador)
        return s
    
    def __mul__(self,fracao1):
        novo_numerador=self.numerador*fracao1.numerador
        novo_denominador=self.denominador*fracao1.denominador

        return fracao(novo_numerador,novo_denominador)
    


f1= fracao(1,2)
f2= fracao(3,2)
#f3= f1.__mult__(f2) se def__mult__
f3=f1*f2 
print (f3)




    

f1=fracao(2,3)
f2=fracao(5,2)
f3=f1.mult(f2)

print(f1,'x',f2,'=',f3)
print(mmc(,))




