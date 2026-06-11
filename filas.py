##A partir do exemplo anterior da “Pilhas” definir a representação e
##operações (métodos) sobre “Filas” 
## Representação de dados: 
##o List 
## Métodos principais: 
## Criar lista vazia 
## Coloca (enqueue) (insere elemento no fim) 
## Retira (dequeue) (retira elemento do início) 
## Início – Devolve elemento no início da fila 
## Comprimento – número de elementos

'''class Fila:
    def __init__(self):
        self.lista=[]
        
    def mostrar_lista(self):
        return self.lista    

    def inicio(self):
        return self.lista[0]

    def coloca(self,elemento):
        self.lista.append(elemento)

    def retira(self):
        return self.lista.pop(0)

    def comprimento(self):
        return len(self.lista)

f= Fila()
f.coloca('primeiro')
f.coloca('segundo')
f.coloca('terceiro')

print('lista em ordem',f.mostrar_lista(),'comprimento',f.comprimento)
print('retirar um elemento',f.retira())
print('lista em ordem',f.mostrar_lista(),'comprimento',f.comprimento)
print('retirar um elemento',f.retira())
print('lista em ordem',f.mostrar_lista(),'comprimento',f.comprimento)'''
    


##2. Simular uma fila de impressão: 
## função adicionar_documento(nome_ficheiro): 
## função imprimir_proximo(): #imprime e retira da fila 
## função mostrar_estado() #mostra nº documentos na fila e quais

'''class FilaImpressao:
    
    def __init__(self):
        self.fila=[]

    def mostrar_fila(self):
        return self.fila

    def para_imprimir(self,arquivo):
        return self.fila.append(arquivo)

    def retira(self):
        return self.fila.pop(0)
    
    def comprimento(self):
        return len(self.fila)


imprimir= FilaImpressao()
imprimir.para_imprimir('imagen.jpg')
imprimir.para_imprimir('arquivo.pdf')
imprimir.para_imprimir('documento.txt')

print('fila da impressão',imprimir.mostrar_fila())
print('retira documento da lista',imprimir.retira())
print('fila da impressão',imprimir.mostrar_fila())
print('retira documento da lista',imprimir.retira())
print('fila da impressão',imprimir.mostrar_fila())'''


##3. Simular um dia nas urgências. (Desafio) 
## a cada minuto a probabilidade de entrar um doente é de 30% 
## a cada minuto a probabilidade de dar alta a um doente é de 20% 
## simular o funcionamento num dia entre as 00h e as 05h da manhã.

import random

p_entrada = 0.30
p_alta = 0.20

doentes = 0
historico = []


for minuto in range(300):
    hora = minuto // 60
    minuto_hora = minuto % 60
    timestamp = f"{hora:02d}:{minuto_hora:02d}"

    evento = []
    #entrada
    if random.random() < p_entrada:
        doentes += 1
        evento.append("Entrada")

    # Alta 
    if doentes > 0 and random.random() < p_alta:
        doentes -= 1
        evento.append("Alta")

    if not evento:
        evento = ["Sem alterações"]

    historico.append((timestamp, evento, doentes))

# resultados
for t, ev, total in historico:
    print(f"{t} — {', '.join(ev)} — Total: {total}")

print("\nDoentes presentes às 05h00:", doentes)




        

