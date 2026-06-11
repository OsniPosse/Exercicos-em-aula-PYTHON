##def calcular_pascoa(ano):
##    x=24
##    y=5
##    a=ano % 19
##    b= ano % 4
##    c= ano % 7
##    d=(19*a+x) % 30
##    e=(2*b+4*c+6*d+y) % 7
##    if(d+e)<10:
##        dia=d+e+22
##        mes='março'
##    else:
##        dia=d+e-9
##        mes='abril'
##    return dia, mes
##
##ano=int(input('digite o ano: '))
##dia, mes=calcular_pascoa(ano)
##print('em', ano,'a pascoa sera dia: ',dia,' de ',mes,)

##def pascoa(ano):
##    match ano:
##        case ano>1582 and ano<1699:
##            x=22
##            y=2
##        case  ano >1700 and ano<1799:
##            x=23
##            y=3
##        case  ano>1800 and ano<1899:
##            x=23
##            y=4
##        case ano>1900 and ano<2099:
##            x=24
##            y=5
##        case  ano> 2100 and ano<2199:
##            x=24
##            y=6
##        case  ano > 2200 and ano<2299:
##            x=25
##            y=7
##            case_:
##            print('ano fora do intervalo')
##
##    a=ano % 19
##    b= ano % 4      
##    c= ano % 7
##    d=(19*a+x) % 30
##    e=(2*b+4*c+6*d+y) % 7
##    if a<10 and d==28 and dia==25 and mes == 'abril':
##        dia=18
##        mes='abril'
##    
##
##ano=int(input('digite o ano: '))
##dia, mes=calcular_pascoa(ano)
##print('em', ano,'a pascoa sera dia: ',dia,' de ',mes,)


def calcular_pascoa(ano):
    
    x, y = 0, 0
    
    match ano:
        case _ if 1583 <= ano <= 1699:
            x, y = 22, 2
        case _ if 1700 <= ano <= 1799:
            x, y = 23, 3
        case _ if 1800 <= ano <= 1899:
            x, y = 23, 4
        case _ if 1900 <= ano <= 2099:
            x, y = 24, 5
        case _ if 2100 <= ano <= 2199:
            x, y = 24, 6
        case _ if 2200 <= ano <= 2299:
            x, y = 25, 7
        case _:
            return None, "Ano fora do intervalo suportado"

    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = (19 * a + x) % 30
    e = (2 * b + 4 * c + 6 * d + y) % 7

    # Determinação do dia e mês
    if (d + e) < 10:
        dia = d + e + 22
        mes = "março"
    else:
        dia = d + e - 9
        mes = "abril"

    # Exceções especiais do algoritmo
    if mes == "abril":
        if dia == 26:
            dia = 19
        if dia == 25 and d == 28 and e == 6 and a > 10:
            dia = 18

    return dia, mes

ano_input = int(input('Digite o ano: '))
dia, mes = calcular_pascoa(ano_input)

if dia:
    print(f'Em {ano_input}, a Páscoa será dia {dia} de {mes}.')
else:
    print(mes)

