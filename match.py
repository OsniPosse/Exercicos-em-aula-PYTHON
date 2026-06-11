def diasemana(n):
    match n:
        case 1 | 7:
            return ("fim de semana")
        case 2 | 3 | 4 | 5 | 6:
            return ("dia de semana")
        case _:
            return ("dia invalido")
        

def semaforo(str):
    match str:
        case "vermelho":
            return ("pare")
        case "amarelo":
            return ("atenção")
        case "verde":
            return ("siga")
        case _:
            return ("cor invalida")  
             
#cor=str(input('digite a cor do semaforo: '))
#dia=int(input('digite:'))
#print(diasemana(dia))
#print(semaforo(cor))

