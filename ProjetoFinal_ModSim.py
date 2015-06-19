from scipy.integrate 
import odeint
from numpy 
import linspace
import matplotlib.pyplot as plt

Vx0 = 13.58   # Velocidade incial X do projétil (m/s)
Vy0 = 13.58   # Velocidade incial X do projétil (m/s)
m = 0.4      # Massa da projétil (kilograma)
ro = 1.2     # Densidade do ar (kg/m**3)
Ca = 0.4     # Coeficiente de arrasto))
g = 9.8      # Aceleração da gravidade (m/s**2)
x0 = 0       # Posição incial do projétil eixo X)
y0 = 0       # Posição incial do projétil eixo Y)))

"""Equações diferenciais"""

def dxdt(Vx, t): # Distância percorrida no eixo X)    )
    dxdt = Vx    
        return dxdt

def dydt(Vy, t): # Distância percorrida no eixo Y)    
    dydt = Vy
        return dydt

def dvxdt(fx,t): # Velocidade no eixo X)
    dvxdt = fx/m   
        return dvxdt    

def dvydt(fy,t): # Velocidade no eixo Y)   )
    dvydt = fy/m   
        return dvydt

def VelocidadeVetorial(vx,vy,t): # Velocidade Vetorial)    )
    v = (vx**2 + vy**2)**0.5)    )
        return v

def ResistX(v,vx,t):             # Força da resistência do ar no eixo X)   )
    fx = -0.5*Ca*ro*A*v*vx
        return ResistX

def ResistY(v,vy,t):             # Força da resistência do ar no eixo Y)
    fy = -0.5*Ca*ro*A*v*vy*m*g))    
        return fy

T = linspace(0,250,251)    
Y = odeint(func, A0, T)