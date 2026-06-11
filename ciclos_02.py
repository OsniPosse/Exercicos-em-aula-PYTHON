##Ciclo “For” 
##1. Escrever os números inteiros ímpares entre 1 e n (inserido pelo utilizador) 

'''n = int(input('Digite um número: '))

if n <=1:
    print("Por favor, insira um número maior que 0.")
else:
    for i in range(1,n+1,2):
        print(i)    '''        
        
        
##2. Somar os números pares entre 0 e n (inserido pelo utilizador).
'''n = int(input('Digite um número: '))
soma=0
if n < 0:
    print("Por favor, insira um número maior que 0.")
else:
    for i in range(0, n + 1, 2):
        soma+=i
    print(soma)   ''' 
        


##3. Escrever a tabuada de um número n (inserido pelo utilizador, entre 1 e 9)

'''n = int(input("escreva um numero"))

if n<0:
    print("Por favor, insira um número maior que 0.")
else:
    
    for i in range(1,11):
        m=n*i
        print(n, " X ", i, " = ",m)'''



##4. Escrever todos os números inteiros entre um número n e um número m (em que n < m) 

'''n = int(input('Digite o valor de n (início): '))
m = int(input('Digite o valor de m (fim): '))

if n >= m:
    print("Erro: n deve ser menor que m.")
else:

    for i in range(n, m+1):
        print(i)'''


##5. Somar todos os números inteiros entre um número n e um número m (em que n < m)
'''n = int(input('Digite o valor de n (início): '))
m = int(input('Digite o valor de m (fim): '))

if n >= m:
    print("Erro: n deve ser menor que m.")
else:

    for i in range(n, m+1):
        print(i+i)'''


##6. Calcular (e escrever) o fatorial de um número n (inserido pelo utilizador, entre 0 e 10) 
'''n = int(input("escrever um numero entre 0 e 10: "))
fat=1
for i in range(1,n+1):
        fat=fat*i
        print(fat)'''
    
    



'''fat = 1
n = int(input("escrever um numero entre 0 e 10: "))
while True:    
    fat = fat * n
    n = n - 1
    print("seu fatorial é: " + str(fat))
    if n <= 1: break'''


##Ciclo “Do… While”

##7. Ler números inteiros e contá-los. Perguntar no fim de cada ciclo ao utilizador se quer sair
##(Insira “S” para sair… qualquer outra para continuar)
'''n=int(input('escrever um numero '))
cont=0
while True:
    cont=cont+1

    s=str(input(' se desejar sair digite  "S" '))
    if s== 's':
        break
print(cont)'''
    
##8. Ler números inseridos pelo utilizador. Contar todos os números inseridos e calcular a sua 
##soma. Perguntar no fim de cada ciclo ao utilizador se quer continuar (Insira “C” para 
##continuar… qualquer outra para sair)

'''cont=0
soma=0
while True:
    n=int(input('escrever um numero  '))
    cont=cont+1
    soma=soma+cont
    
    sair=str(input('Insira “C” para continuar… qualquer outra para sair'))
    if sair!='c':
        break
print('numeros contatdos: ', cont,' as soma dos numeros contados ',soma)'''
    
    
##9. Ler números inteiros positivos inseridos pelo utilizador. Guardar o número maior inserido 
##pelo utilizador. Perguntar no fim de cada ciclo ao utilizador se quer sair (Insira “S” para sair… 
##qualquer outra para continuar) 

'''maior=0
while True:
    n=int(input('insira um numero:'))
    if n>maior:
        maior=n

    sair=input('Insira “S” para sair… qualquer outra para continuar')
    if sair=='s':
        break
print(maior)'''    
        
             
         






