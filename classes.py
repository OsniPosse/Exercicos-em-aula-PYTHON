# 07/05

#paradigmas
#programa imperativa
#programa funcional
#programa objetos

'''def idade(dt_nasc):
    def aniver(mes_ani,dia_ani):#função dentro de função
        return true

    
    idade=ano_atual-ano_nasc-1+aniver()'''

'''1. Definir a classe ‘livro’, com os atributos título e autor 
2. Definir a classe ‘telemóvel’, com os atributos marca, modelo e memória 
Criar objetos 
3. Criar dois livros 
4. Criar dois telemóveis 
Visualizar objetos 
1. Visualizar (com print) os dois livros criados 
2. Visualizar (com print) os dois telemóveis criados '''

'''class Livro:
    # Correção: __init__ com dois underscores
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
livro1 = Livro('O Alquimista', 'Paulo Coelho')
livro2 = Livro('1984', 'George Orwell')

print(f'O título do livro: {livro1.titulo}, do autor: {livro1.autor}')

class Telemovel:
    # Correção: __init__ com dois underscores
    def __init__(self, marca, modelo, memoria):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria

telemovel1 = Telemovel('iPhone', '15 Pro Max', '512GB')

print(f'Marca: {telemovel1.marca}, Modelo: {telemovel1.modelo}, Memória: {telemovel1.memoria}')


class livro:
    
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
        
livro1=livro('O Alquimista','Paulo Coelho')
livro2=livro('1984','George Ornewl')

print('o titlulo do livro: ',livro1.titulo,'do autor: ',livro1.autor)

class telemovel:
    def __init__(self,marca,modelo,memoria):
        self.marca=marca
        self.modelo=modelo
        self.memoria=memoria


telemovel1=telemovel('iphone','promax','520G')
telemovel2=telemovel('xiaome','redmi15','280G')
telemovel3=telemovel('samsung','s23','520G')

print('marca do telemovel: ',telemovel1.marca,'modelo: ',telemovel1.modelo,'memoria: ',telemovel1.memoria)'''



'''Classe ‘conta bancária’ 
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


class conta_bancaria:
    
    
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
'''
print(conta1.levantamento(600))  # Retorna erro de saldo insuficiente
print(conta1.levantamento(100))  # Funciona corretamente
print(conta1.consulta()) '''


    
def E_conta(conta):
    return isinstance(conta, conta_bancaria)
    
print("conta existente:",E_conta(conta1))
print("saldo atual:",conta1.consulta())
print("valor do deposito:",conta1.deposito(100))
print("valor a ser levantado:",conta1.levantamento(150))

print("saldo atual:",conta1.consulta())

        

        
