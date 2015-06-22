from math import *
from numpy import linspace
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def func2(Z,t):
    yp = A * sin( (2*pi*v*t)/x )
    dypdt = A * cos( 2*pi*v*t/x ) * ( (2*pi*v)/x )
    
    dz1dt = Z[1]
    dz2dt = ( ((4*K)/m) * (yp - Z[0]) ) + ( ( (4*d)/m ) * (dypdt - Z[1]) )
    return [dz1dt, dz2dt]

K = 80000
d = 350
m = 1500
A = 0.1
x = 1
v = 10


z10 = 0
z20 = 0
Z0 = [z10, z20]
T1 = linspace(0,30,3000001)
T2 = linspace(0,10,1000001)

Z1 = odeint(func2, Z0, T1)

middle = Z1[:,0]
ZMaxA = middle[2500000:]
amplitude = min(ZMaxA)



plt.plot(T1, Z1[:,0],'r')
plt.axhline(amplitude,0,30)

plt.xlabel('Tempo (s)')
plt.ylabel('Deslocamento vertical do carro (m)')
plt.show()
