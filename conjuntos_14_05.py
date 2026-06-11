'''conjuntos:   
lista=list(set([1,2,2,3,4,4]))
print (lista)'''

# Listas iniciais de convidados 
'''faculdade = {"Ana", "Bruno", "Carlos", "Diana"} 
trabalho = {"Carlos", "Diana", "Eduardo", "Fernanda"} 
Escreva o código em Python para resolver os seguintes passos: 

1. União: Crie uma lista única chamada total_convidados com todas as pessoas convidadas, sem 
repetições. 
faculdade = {"Ana", "Bruno", "Carlos", "Diana"} 
trabalho = {"Carlos", "Diana", "Eduardo", "Fernanda"} 
total_convidados=list(set(trabalho|faculdade))
print(total_convidados)

2. Interseção: Descubra quem são as pessoas que pertencem a ambos os grupos (amigos da faculdade 
que também trabalham consigo) e guarde em amigos_comuns. 
faculdade = {"Ana", "Bruno", "Carlos", "Diana"} 
trabalho = {"Carlos", "Diana", "Eduardo", "Fernanda"}
amigos_comum=list(set(faculdade & trabalho))
print(amigos_comum)

3. Diferença: Descubra quem são as pessoas exclusivas da faculdade (que não trabalham consigo) e 
guarde em apenas_faculdade. 
faculdade = {"Ana", "Bruno", "Carlos", "Diana"} 
trabalho = {"Carlos", "Diana", "Eduardo", "Fernanda"}
apenas_faculdade=list(set(faculdade-trabalho))
print(apenas_faculdade)

4. Adicionar: À última hora, o seu amigo "Gustavo" confirmou que ia. Adicione-o ao conjunto 
total_convidados.
faculdade = {"Ana", "Bruno", "Carlos", "Diana"} 
trabalho = {"Carlos", "Diana", "Eduardo", "Fernanda"} 
total_convidados=list(set(trabalho|faculdade))
total_convidados.append("Gustavo")
print(total_convidados)

5. Remover: A "Diana" avisou que não vai poder ir. Remova-a do conjunto total_convidados.
faculdade = {"Ana", "Bruno", "Carlos", "Diana"} 
trabalho = {"Carlos", "Diana", "Eduardo", "Fernanda"} 
total_convidados=list(set(trabalho|faculdade))
total_convidados.remove("Diana")
print(total_convidados)'''
