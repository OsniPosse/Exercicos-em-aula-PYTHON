'''f=open("C:ficheiro.txt ",'r')
lista=f.readlines()
numeros = [int(linha.strip()) for linha in lista]
f.close()
        
minimo=[]
maximo=[]
for n in numero:
    if n<numero:
        minimo=n
    if n>numero:
        maximo=n
print(minimo)
print(maximo)'''

"""
para ecrita de arquivos
open('dados.txt', 'w') --cria um novo ficheiro
open('dados.txt', 'a') -- altera ficheiro existente  sempre na ultima linha
arquivo.write(str)--devolve o numero de caractres escritos
print(...,file=arquivo)--pra pular linha'\n'

ficheiros .csv tambem é possivel manipular
"""
f=open("C:ficheiro1.txt ",'w')
f.write('osni\nposse\nfonseca\nduarte')
f.close()

f=open("c:ficheiro1.txt",'r')
str=f.read()
print(str)
f.close()


f=open("C:ficheiro1.txt ",'a')
f.write('\nwgreg',file=f)
f.close()

f=open("c:ficheiro1.txt",'r')
str=f.read()
print(str)
f.close()

'''cont=f.readlines()

contar=0
for i in cont:
    
    contar=contar+1
    media=sum(cont)/len(cont)
print("quantidade de temperaturas inseridas: ",contar)
print("teperatura minima: ",min(cont))
print("temperatura maxima: ",max(cont))
print("temperatura maxima: ",media)'''

'''
# 1. Abrir o ficheiro e ler as linhas
with open('dados.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# 2. Transformar as linhas (texto) em números inteiros
# O .strip() remove espaços ou quebras de linha invisíveis
numeros = [int(linha.strip()) for linha in linhas]

# 3. Extrair as estatísticas
maximo = max(numeros)
minimo = min(numeros)
media = sum(numeros) / len(numeros)

# Mostrar resultados
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Média: {media}")
'''
