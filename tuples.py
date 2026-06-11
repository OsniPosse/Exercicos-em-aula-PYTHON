def print_elems(t):
    for i in t:
          print(i)


def dobra_elems(t):
    cont=0
    for i in t:
        cont += i*2
    return cont

def soma_elems(t):
    cont=0
    for i in t:
        cont += i
    return cont


def maior_elems(t):
    maior = t[0]
    for i in t:
        if i > maior:
            maior = i
    return maior

t=(1,2,3,4,5,6)
#print(print_elems(t))
#print(dobra_elems(t))
#print(soma_elems(t))
#print(maior_elems(t))


