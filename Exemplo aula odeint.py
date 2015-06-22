
from math import *
from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt

m=1
g=10
Cd=0.47
p=1
A=10**(-2)
   

def func(X,t):
    
    Vx=X[0]
    Vy=X[2] 
    
    Vq=(Vx**2)+(Vy**2)
    V=sqrt(Vq)
    
    dVxdt=(p*Cd*A*Vq*Vx/(V))*(-1/2*m)
    dVydt=((p*Cd*A*Vq*Vy/V)*(-1/2*m))-g
    
    return [dVxdt, x, dVydt, y]
V0=100
teta = 45
teta = teta/360*2*math.pi

X0=[V0*cos(teta), 0, V0*sin(teta), 0]

t=linspace(0,14.1, 1001)

X=odeint(func,X0,t)

plt.plot(X[:,1],X[:,3])
plt.show()
    