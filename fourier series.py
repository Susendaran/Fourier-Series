import math as m
from matplotlib import pyplot as plt
def ft(k,t):
    if t>0 and t<4:
        func=2-t
    elif t>4 and t<8:
        func=t-6
    return func


def simpson(f,k):
    a=0.01
    b=8
    n_p=1000
    h=(b-a)/n_p
    summ=0
    x0=a
    x1=x0+h
    x2=x1+h
    if n_p%2==1:
        x3=x2+h
        summ=summ + (f(k,x0) + 3*f(k,x1) + 3*f(k,x2) + f(k,x3))*((3*h)/8)
        x0=x3
        x1=x0+h
        x2=x1+h
        
    while x2<b:
        if(x2!=4 and x0!=4 and x1!=4):
            summ=summ + (f(k,x0) + 4*f(k,x1) + f(k,x2))*(h/3) 
        x0=x2
        x1=x0+h
        x2=x1+h
    return summ


def A(k,t):
    ak=ft(0,t)*m.cos((2*m.pi*t*k)/8)
    return ak

def B(k,t):
    bk=ft(0,t)*m.sin((2*m.pi*t*k)/8)
    return bk

n=10

dt=0.01
t0=0.01
x=[]
y=[]
x_f=[]
y_f=[]
A0=simpson(ft,0)/8
print("A0=",A0)
while t0<8:
    print(t0)
    if t0!=4:
        x.append(t0)
        x_f.append(t0)
        y.append(ft(0,t0))
    yf=A0
    for i in range(1,n):
        Ak=(2/8)*simpson(A,i)
        Bk=(2/8)*simpson(B,i)
        if t0!=4:
            yf=yf+(Ak*m.cos(i*(2*m.pi/8)*t0)+Bk*m.sin(i*(2*m.pi/8)*t0))
    y_f.append(yf)
    t0+=dt

plt.plot(x,y)
plt.show()
plt.plot(x_f,y_f)
plt.show()