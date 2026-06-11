'''def bissexto(ano):
    
    if (ano%400==0):
        return True
    
    elif (ano%100==0):
          return False
        
    elif (ano%4==0): 
        return True
    else:
        return False


ano=int(input("digite o ano"))
print(bissexto(ano))'''


def bi6(ano):
    return (ano%4==0 and not(ano%100==0)) or ano%400==0

print (bi6(2000))
