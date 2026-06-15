# defina uma função que conte o numero de caracteres de uma string
'''def conta_c(s):
    cont=0
    for i in s:
        cont=cont+1
    return cont    
        
l='abcd'
print(conta_c(l))'''

#definir uma funçao   val_hex que receba uma string tudo maisculo
#e como resultado true ou false para numero decimal
'''def val_hex(s):

    return s in "ABCDEF"


entrada = input("Digite uma letra maiúscula: ")
print(val_hex(entrada))'''


#escreva um programa que leia 5 notas para uma lista de inteiros e faça print da média, nota mais baixa nota mais alta, sem usar a função len ou qualquer outra função sobre listas
'''n = []
soma = 0
maior=0
menor=20


for i in range(5):
    n = int(input("Digite a nota : "))   
    soma += n
    if n<menor:
        menor=n
    if n>maior:
        maior=n


        
    
media = soma / 5

print("Média: ",media)
print("Nota mais baixa: ",menor)
print("Nota mais alta: ",maior) '''


#tranforme MPG em litros/100km
'''mpg=57
milhakm=1.61
g=3.79
consumo


consumo= milhakm*mpg/galao
print("resultado: ",100/consumo)'''



#escreva um programa que pergunte o diametro de duas pizzas de tamanhos diferentes, e de a resposta de qual tem maior área
'''d1 = float(input("Diâmetro da pizza grande (cm): "))
d2 = float(input("Diâmetro da pizza familia (cm): "))
pi=3.14

area1 =( pi * (d1 / 2)**2)*2
area2 = pi * (d2 / 2)**2

print("Área de duas pizzas grande: cm²",area1)
print("Área da pizza familia: cm²",area2)


if area1 > area2:
    print("duas pizzas grande tem maior area, tem mais pizza.")
elif area2 > area1:
    print("uma pizza familia tem mais pizza.")
else:
    print("As duas pizzas têm o mesmo tamanho.")'''


#definir uma função que receba um byte(8bits, como string)e retorne o valor em decimal
'''def byte_para_decimal(byte_str):
    decimal = 0
    expoente = 7
    for bit in byte_str:
        decimal += int(bit) * (2 ** expoente)
        expoente -= 1
    return decimal

meu_byte = str(input("Digite um byte (8 bits): "))
print("O valor decimal de ", meu_byte, " é ", byte_para_decimal(meu_byte))'''


#definir uma funçao para validar um NIF(string)sendo CD o check digite que é o 9º digito, 
#multiplicar os 8 primeiro digitos ,somar os produtos, calcular o resto da divisão sa soma por 11
#se for 0 ou 1, cd deve ser 0, senão o cd é igualao resto da divisão
'''def validar_nif(nif):
      if len(nif) != 9 or not nif.isdigit():
        return False
    soma = 0
  
    for i in range(8):
        
        soma += int(nif[i]) * (9 - i)

        resto = soma % 11

    if resto == 0 or resto == 1:
        cd_esperado = 0
    else:
        cd_esperado = 11 - resto

    
    return int(nif[8]) == cd_esperado


nif_input = input("Digite o NIF para validar: ")
if validar_nif(nif_input):
    print("NIF Válido!")
else:
    print("NIF Inválido.")'''

#definir uma função que leia a data (como string  no formato ddmmaaaa,e admitindo que é valida)
# e calcule a idade(inteiro) ádata de hoje(27042026)

'''def calcular_idade(data_nasc):
   
    dia_n = int(data_nasc[:2])
    mes_n = int(data_nasc[2:4])
    ano_n = int(data_nasc[4:])
       
    dia_hoje, mes_hoje, ano_hoje = 27, 4, 2026
       
    idade = ano_hoje - ano_n
        
    if (mes_hoje < mes_n) or (mes_hoje == mes_n and dia_hoje < dia_n):
        idade -= 1
        
    return idade

data = input("Digite a data de nascimento (ddmmaaaa): ")
print("Idade em 27/04/2026:  anos",calcular_idade(data))'''

#complete o codigo lista_troco contenha, no final a quantidade de
#notas e moedas a devolver como troco. Admita que o preço dos bilhetes é igua a 1euro e
#que o valor entregue é um inteiro natural
'''num_bilhetes = int(input('insira o numero de bilhetes: '))
valor_entregue = int(input('insira o valor entregue: '))
tuple_dinheiro = (20, 10, 5, 2, 1)
lista_troco = [0, 0, 0, 0, 0]


troco_total = valor_entregue - (num_bilhetes * 1)

for i in range(len(tuple_dinheiro)):
   
    lista_troco[i] = troco_total // tuple_dinheiro[i]
    
    troco_total = troco_total % tuple_dinheiro[i]

print("Quantidade de notas/moedas (20€, 10€, 5€, 2€, 1€): ",lista_troco)'''

'''
Classe ‘conta bancária’ 
Modelar de forma simplificada uma conta bancária, apenas pelo seu saldo (ignorando todas as outras 
características reais como: número, titular, banco, agência 
Considerar também as seguintes operações básicas: 
 Construtores 
o Cria conta (inteiro* > conta) 
 Seletores 
o Consulta (conta > inteiro) 
 Modificadores 
o Deposito (conta x quantia > quantia) 
o Levantamento (conta x quantia > quantia) 
 Reconhecedores 
o E_conta (conta > Bool) #utilizar ‘isinstance(obj, class) > bool’ '''


'''class conta_bancaria:
    
    
    def __init__(self,conta,saldo):
        self.conta=conta
        self.saldo=saldo

    def consulta(self):
        return self.saldo    
        
    def deposito(self,quantia):
        self.saldo+=quantia
        return quantia
    
    def levantamento(self,quantia):
        self.saldo-=quantia
        return quantia
    
conta1=conta_bancaria(1,500)



    
def E_conta(conta):
    return isinstance(conta, conta_bancaria)
    
print("conta existente:",E_conta(conta1))
print("saldo atual:",conta1.consulta())
print("valor do deposito:",conta1.deposito(100))
print("valor a ser levantado:",conta1.levantamento(150))

print("saldo atual:",conta1.consulta())'''

mpg=57
milhakm=1.61
g=3.79
consumo=mpg*milhakm/g
print("mpg em 100klm: ",100/consumo)
