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

K = 10 # Vibração inicial
d = 1   # 
m = 1  # Massa (gramas)
A = 0.1   # Área lateral (m**2)
x = 1     # Amplitude (metros)
v = 100    # Velocidade incial


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

plt.xlabel('Distância (m)')
plt.ylabel('Vibração da munição (m)')
plt.show()





#==============================================================================
"""pré-modelo"""
#from scipy.integrate 
#import odeint
#from numpy 
#import linspace
#import matplotlib.pyplot as plt
#
# Vx0 = 13.58   # Velocidade incial X do projétil (m/s)
# Vy0 = 13.58   # Velocidade incial X do projétil (m/s)
# m = 0.4      # Massa da projétil (kilograma)
# ro = 1.2     # Densidade do ar (kg/m**3)
# Ca = 0.4     # Coeficiente de arrasto))
# g = 9.8      # Aceleração da gravidade (m/s**2)
# x0 = 0       # Posição incial do projétil eixo X)
# y0 = 0       # Posição incial do projétil eixo Y)))
#
# """Equações diferenciais"""
#
# def dxdt(Vx, t): # Distância percorrida no eixo X)    )
#     dxdt = Vx    
#         return dxdt
#
# def dydt(Vy, t): # Distância percorrida no eixo Y)    
#     dydt = Vy
#         return dydt
#
# def dvxdt(fx,t): # Velocidade no eixo X)
#     dvxdt = fx/m   
#         return dvxdt    
#
# def dvydt(fy,t): # Velocidade no eixo Y)   )
#     dvydt = fy/m   
#         return dvydt
#
# def VelocidadeVetorial(vx,vy,t): # Velocidade Vetorial)    )
#     v = (vx**2 + vy**2)**0.5)    )
#         return v
#
# def ResistX(v,vx,t):             # Força da resistência do ar no eixo X)   )
#     fx = -0.5*Ca*ro*A*v*vx
#         return ResistX
#
# def ResistY(v,vy,t):             # Força da resistência do ar no eixo Y)
#     fy = -0.5*Ca*ro*A*v*vy*m*g))    
#         return fy
#
# T = linspace(0,250,251)    
# Y = odeint(func, A0, T)