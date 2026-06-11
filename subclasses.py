##SubClasses 
##Classe ‘conta genérica’ (conta_gen) 
##Guia Prático 
##Modelar de forma simplificada uma conta bancária, apenas pelo seu saldo e saldo mínimo permitido 
##(ignorando todas as outras características reais como: número, titular, banco, agência 
##Métodos: 
## Seletores 
##o Consulta (conta > inteiro) 
## Modificadores 
##o Deposito (conta x quantia > quantia) 
##o Levantamento (conta x quantia > quantia) até atingir saldo mínimo 
##SubClasse ‘conta ordenado’ (conta_ord) + ‘conta jovem’ (conta_jov) 
##Métodos: 
## Construtores 
##o Cria conta (inteiro* > conta) 
##Interações ‘conta bancária’ 
##conta_ord_01=conta_ord(300,500) 
##o saldo inicial deve ser maior ou igual ao valor do ordenado 
##conta_ord_01=conta_ord(800,500) 
##conta_ord_01.levantamento(500) 
##300 
##conta_ord_01.levantamento(500) -200 
##conta_jov_01=conta_jov(50) 
##conta_jov_01.consulta() 
##50 
##conta_jov_01.levantamento(100) 
##saldo insuficiente 
##*Simplificando também que os montantes correspondem a números inteiros.   

class conta_gen:
    def consulta(self):
        return self.saldo      
        
    def deposito(self,quantia):
        self.saldo+=quantia
        return quantia
    
    def levantamento(self,quantia):
        self.saldo-=quantia
        return quantia

class conta_ordenado(conta_gen):
    def __init__(self,saldo,ordenado):
        if saldo<ordenado:
            print("saldo percisa ser maior ou igual ao ordenado")
        self.ordenado=ordenado
        self.saldo_min=-ordenado
        
        

class conta_joven(conta_gen):
    def __init__(self,saldo):
            self.saldo=saldo
             self.saldo_min=0
        
            
conta_ord1 = conta_ordenado(800, 500)
print("Saldo atual ordenado:", conta_ord1.consulta()) # Retorna 800

conta_ord1.levantamento(500)
print("Saldo após levantamento 1:", conta_ord1.consulta()) # Retorna 300

conta_ord1.levantamento(500)
print("Saldo após levantamento 2 (descoberto):", conta_ord1.consulta()) # Retorna -200

# 2. Teste Conta Jovem
conta_jov1 = conta_joven(50)
print("Saldo atual jovem:", conta_jov1.consulta()) # Retorna 50
print("Tentativa de levantamento excessivo:", conta_jov1.levantamento(100))
        
        
