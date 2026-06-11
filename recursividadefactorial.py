#recursividade


def fact(n):
    print(n)
    return(n*fact(n-1))



'''
baseline
if n==1:
  return(1)
return(n*fact(n-1))
'''
print(fact(5))


'''
funções recursivas
factorial_r(n)
soma_n_r(lim_inf,lim_sup)
mult_r(mult1,mult2)
pot_r(base,exp)
'''
