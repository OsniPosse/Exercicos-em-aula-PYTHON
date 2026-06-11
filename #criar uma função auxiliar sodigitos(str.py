#criar uma função auxiliar sodigitos(str, que retorna True caso a string apenas tenha dígitos
def sodigitos(s):
        return s.isdigit()


def nomecompleto(n):
    if len(nome)<5:
        return False
    else:
         return True


def idiefp(i):
       if len(id) == 9 and sodigitos(id):
        return True
       else:
           return False

def valid_email(e):
    
    if '@formacao.iefp.pt' != email[-17:]:
        return False   
    username = email[:-17]   
    if len(username) == 0:
         return False   
    return True


def datanascimento(d):
    if len(data) != 10 or data[2] != '/' or data[5] != '/':
        return False
    return True
        
  


nome=input('digite o primeiro e ultimo nome: ')
print(nomecompleto(nome))
id=input('digite o numero de registro IEFP com 9 digitos: ')
print(idiefp(id))
email=input('digite seu email da formação: ' )
print(valid_email(email))
data=input('digite sua data de nascimento formato dd/mm/aaaa: ')
print(datanascimento(data))
