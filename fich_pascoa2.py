import datetime

def calcular_pascoa(ano):
    
    x, y = 24, 5
    a = ano % 19
    b = ano % 4
    c = ano % 7
    d = (19 * a + x) % 30
    e = (2 * b + 4 * c + 6 * d + y) % 7
    
    if (d + e) < 10:
        dia = d + e + 22
        mes = 'março'
    else:
        dia = d + e - 9
        mes = 'abril'
        
        if dia == 26: dia = 19
        if dia == 25 and d == 28 and a > 10: dia = 18
            
    return dia, mes

ano_atual = datetime.datetime.now().year


with open("c:/Users/ivani/OneDrive/Área de Trabalho/ADS/PHYTON/fich_pascoa.csv", "w", encoding="utf-8") as f:
    f.write("Ano;Dia;Mes\n") 
    for i in range(50):
        ano_alvo = ano_atual + i
        dia, mes = calcular_pascoa(ano_alvo)
        f.write(f"{ano_alvo};{dia};{mes}\n")

print("Ficheiro 'fich_pascoa.csv' gerado com sucesso para os próximos 50 anos!")
