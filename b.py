import numpy as np
a=float(input('a:'))
b=float(input('b:'))
xi=float(input('error:'))
def f(x):
    f=2*np.sin(np.pi*x)+np.cos(np.pi*x)
    return f
nothing=0
k=0
while nothing==0:
    if f(a)*f(b)>0:
        print('wrong')
        break
    elif f(a)*f(b)==0:
        if f(a)==0:
            k=k+1
            print(a,k)
            break
        else:
            k=k+1
            print(b,k)
            break
    else:
        m=0.5*(a+b)
        if abs(a-b)<xi:
            print(m,k)
            break
        else:
            if f(a)*f(m)>0:
                a=m
                k=k+1
            else:
                b=m
                k=k+1