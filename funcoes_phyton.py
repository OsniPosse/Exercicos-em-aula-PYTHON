##Escreva o programa com a seguinte estrutura: 
##A. Código principal: 
##- DECLARAR as variáveis necessárias com um nome sugestivo e respetivo tipo 
##- LER os valores necessários de input do utilizador (dados necessários para processamento). 
##- INVOCAR (CHAMAR) a função com os parâmetros necessários (e só estes). 
##- Utilizar o valor DEVOLVIDO (RETORNO/RETURN) da função para: (o passo seguinte) 
##- ESCREVER o resultado de volta (no ecrã) para o utilizador. 
##B. Código da função: 
##- DECLARAR função, com nome sugestivo, relacionado com a tarefa/sequência de instruções que 
##executa. 
##- DECLARAR os parâmetros da função. Nomes e tipos das variáveis que são dados de entrada 
##(INPUT) na função. 
##- DEFINIR o conjunto de instruções necessárias a executar a tarefa necessária 
##- DEVOLVER (RETORNO/RETURN) o valor que é resultado* da função 
##*Privilegiar tipos numéricos (Int, decimal) e booleanos (V/F) em detrimento de “Texto”. 
##Evitar funções sem RETORNO 

##C. Exercícios: 
##1. Função "MilhaToKm" que recebe um número natural que representa uma distância em 
##milhas e devolve (retorna) essa mesma distância em Km's.

'''def milhatokm(n):
    km=milhas*1.609
    return km

milhas=float(input('insira as milhas: '))
print('as milhas em km',milhatokm(milhas))'''

##2. Função "FtoC". Recebe um temperatura em ºF e retorna essa mesma temperatura em ºC.
'''def FtoC(n):
    c=(f-32)/1.8
    return c
f=float(input('digite o valor em farenheit: '))
print('a temperatura em celcius: ',FtoC(f))'''


##3. Função "maior" que recebe dois números naturais e retorna o maior.
'''def maior(n):
    if n>m:
        return n
    else:
        return m
n=int(input('insira um numero: '))
m=int(input('insira outro numero'))
print('o maior numero é: ',maior(n))'''    


##4. Função "par" que recebe um número natural e retorna se é, ou não, par. (V, F)
'''def par(n):
    if n%2==0:
        n='true'
        return n
    else:
        n= 'false'
        return n

n=int(input('digite um numero para verificar se é par: '))
print('o numero é ',par(n),'para par')'''

##5. Função "IMC". Recebe um número natural que representa o peso (em Kg) e um número 
##decimal que representa uma altura (em metros) e retorna o IMC.
'''def imc(n):
    imc=peso/(altura**2)
    return imc
peso=float(input('digite seu peso: '))
altura=float(input('digite sua altura'))
print('seu IMC é: ',imc(imc))'''

##6. Função "sinal" que recebe um número inteiro e retorna se é "positivo", "negativo" ou "zero"
'''def sinal(n):
    if n>0:
        n='positivo'
        return n
    else:
        if n<0:
            n='negativo'
            return n
        else:
            n='zero'
            return n
n=int(input('digite um numero para saber se é positivo, negativo ou zero: '))
print('o numero é: ',sinal(n))'''

##7. Função "fatorial". Recebe um número natural e retorna o cálculo do fatorial.
'''def fatorial(n):
    fat=1
    while n>1:
        fat=fat*n
        n=n-1
    return fat

n=int(input('digite um numero para obter seu fatorial: '))
print('o fatorial de:',n,'é:',fatorial(n))'''


#8. Função “desconto” que recebe um preço e um desconto em percentagem e devolve o valor 
##a pagar (preço com desconto aplicado).

'''def desconto(p, d):
    d = d / 100 * p
    t = p - d
    
    return t

p = float(input("digite o valor do produto: "))
print()
d = float(input("digite o desconto em porcentagem: "))
print("o preço com desconto é: " ,desconto(p, d))'''

##9. Função "primo" que recebe um número natural e diz se é ou não primo (V/F).

'''def primo(n):
    if n<=1:
            return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        

n = int(input("escreva um numero e descubra se é  numero primo: "))
print("resultado: ",primo(n))'''


##10. Escrever os números primos até N (número inteiro dado pelo utilizador), utilizando a função 
##“primo” do ponto anterior.
def primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True 


n = int(input("Escreva um número para ver todos os primos até ele: "))

print('Números primos até',n,':')

for  i in range(2,n+1):
    if primo(i):
        print(i)


