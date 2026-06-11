# defina uma função que conte o numero de caracteres de uma string

'''def cont(s):
    cont=0
    for i in s:
        cont+=1
    return cont
print(cont('python'))'''

#definir uma funçao   val_hex que receba uma string tudo maisculo
#e como resultado true ou false para numero decimal        
'''def val_hex(s):
    for i in s:
        if i not in '0123456789ABCDEF':
            return False
    return True
print(val_hex('AZ01'))  '''

#escreva um programa que leia 5 notas para uma lista de inteiros e
#faça print da média, nota mais baixa nota mais alta, sem usar a função
#len ou qualquer outra função sobre listas
'''soma=0
n=[]
maior=0
menor=20
for i in range(5):
    nota=int(input('insira a nota da UC: '))
    n=n+[nota]
    soma=soma+nota
    
    if nota>maior:
        maior=nota
    if nota<menor:
        menor=nota
        
media=soma/5

print(n,soma,media,maior,menor)'''
    
#tranforme MPG em litros/100km
'''def mpg(m):
    milha=1.61
    galao=3.79
    consumo=(galao/(milha*m))*100
    return consumo
print(mpg(57))'''

#escreva um programa que pergunte o
#diametro de duas pizzas de tamanhos diferentes, e de a
#resposta de qual tem maior área
'''d1=float(input('tamanho da media'))
d2=float(input('tamanho da grande'))
pi=3.14
area_d1=(pi*(d1/2)**2)*2
print(area_d1)
area_d2=pi*(d2/2)**2
print(area_d2)

if area_d1>area_d2:
    print("duas médias tem maior area do que uma grande")
elif area_d1<area_d2:
    print("uma grande tem maior area que duas media")
else:
    print("as duas tem a mesma area")'''

#definir uma função que receba um byte(8bits, como string)e retorne o valor em decimal
'''def byte_dec(byte):
    e=7
    d=0
    for bit in byte:
        d=d+int(bit)*2**e
        e=e-1
    return d    
    
print(byte_dec('01000001'))'''
    
#definir uma funçao para validar um NIF(string)sendo CD o check digite que é o 9º digito, 
#multiplicar os 8 primeiro digitos ,somar os produtos, calcular o resto da divisão sa soma por 11
#se for 0 ou 1, cd deve ser 0, senão o cd é igualao resto da divisão

'''def validar_nif(nif):
    multiplicador=9
    soma=0
    for i in nif[:-1]:
        soma=soma+multiplicador* int(i)
        multiplicador=multiplicador-1
    resto=soma%11
    if resto==0 or resto==1 :
        cd=0
    else:
        cd=11-resto
    if int(nif[8])==cd:
        return True #return(nif[8]==cd)
    else:
        return False
        
print(validar_nif('501228576'))'''

#definir uma função que leia a data (como string  no formato ddmmaaaa,e admitindo que é valida)
# e calcule a idade(inteiro) a data de hoje(27042026)

'''from datetime import date

def calc_idade(data_nasc):
    
    data_atual=date.today()
    ano_atual=data_atual.year
    mes_atual=data_atual.month
    dia_atual=data_atual.day
    dia_nasc=int(data_nasc[0:2])
    mes_nasc=int(data_nasc[2:4])
    ano_nasc=int(data_nasc[4:8])
    if mes_atual>mes_nasc:
        return ano_atual-ano_nasc
    if mes_atual<mes_nasc:
        return ano_atual-ano_nasc-1
    if dia_atual>=dia_nasc:
        return ano_atual-ano_nasc
    return ano_atual-ano_nasc-1    
    
data_nasc="12061988"            
print(calc_idade(data_nasc))'''


#complete o codigo lista_troco contenha, no final a quantidade de
#notas e moedas a devolver como troco. Admita que o preço dos bilhetes é igua a 1euro e
#que o valor entregue é um inteiro natural
'''bilhete=1
tuple_dinheiro=(20,10,5,2,1)
lista_troco=[0,0,0,0,0]

num_bilhetes=int(input('digite o numero de bilhetes'))
valor_entregue=int(input('digite o valor entregue'))

troco=valor_entregue-num_bilhetes*bilhete
for i in range(len(tuple_dinheiro)):
        lista_troco[i]=troco//tuple_dinheiro[i]
        troco=troco%tuple_dinheiro[i]

print(lista_troco)'''













            
