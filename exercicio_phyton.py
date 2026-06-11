#descubra o dobro
"""n=int(input('digite o valor'))
dobro=n*2
print(dobro)"""

#converter metros em centimetros
"""n=float(input('digite o valor em metros'))
centimetros=n*100
print(centimetros,'centimetros')"""

#converter polegadas em centimentros
"""n=float(input('converter polegadas em centimetros: '))
centimetros=n*2.54
print(centimetros,' centimetros')"""

#valor total bilhetes
"""n=float(input('digite o valor do bilhete: €'))
m=float(input('digitea quantidade de bilhetes: '))
print('o total a pagar:  €',n*m)"""

#perimetro e area do retangulo
"""n=int(input('digite o comprimento do retangulo: '))
m=int(input('digite a largura do retangulo: '))
print('o perimetro do retangulo é: ',2*(n+m))
print('a area do retangulo é: ',n*m)"""

#perimetro e area do quadrado
"""n=int(input('digite o lado do quadrado: '))
print('o perimetro do quadrado é: ',4*n)
print('a area do quadrado é: ',n**2)"""

#valor do produto com IVA
"""n=float(input('digite o valor do produto sem IVA: €'))
m=float(input('digite a taxa do IVA: %'))
t=n*(m/100)
print('o valor do IVA sobre o produto é: €',t)
print('o valor do produto com IVA é: €',n+t)"""

#valor com juros em 1 ano
"""n=float(input('deposito em 01/01/2017: €'))
m=float(input('taxa de juros: %'))
t=n*(m/100)
print('o valor do juro é: €',t)
print('o valor no banco em 01/01/2018 é: €',n+t)"""

#salario liquido
"""n=float(input('salario bruto: €'))
s=float(input('taxa desconto social: %'))
i=float(input('taxa descontoIRS: %'))
ds=n*(s/100)
print('o valor do desconto social é: €',ds)
di=n*(i/100)
print('o valor do desconto IRS é: €',di)
print('o salario liquido é: €',n-ds-di)"""

#consumo combustível
"""litros=float(input('custo por 100km(em litros):  Litros '))
km=float(input('numero de km feitos:  km '))
custolitro=float(input('custo por litro:  €'))
consumo=(km-100)/litros
print('o consumo em litros é:  litros ',consumo)
total=consumo*custolitro
print('o valor total gasto: €',total)"""

#valor consumo energia
"""potencia=float(input('digite a potência do aparelho em watts:  '))
horas=float(input('Digite quantas horas esta usando o aparelho:  '))
custo=float(input('custo em kwh:  €'))
consumo= (potencia/1000)*horas
print('potencia consumida: ',consumo)
total=consumo*custo
print('o valor total gasto: €',total)"""

#IMC
"""peso=float(input('digite seu peso:  kg'))
altura=float(input('digite sua altura:  Mts'))
imc=peso/(altura**2)
print('o IMC é',imc)"""

