# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 09:10:33 2015

@author: lucasmb2
"""

# Implementação do modelo
from scipy.integrate import odeint 
from numpy import linspace
import matplotlib.pyplot as plt

Vx0 = 13.58   # Velocidade incial X do projétil (m/s)
Vy0 = 13.58   # Velocidade incial X do projétil (m/s)
m = 0.4      # Massa da projétil (kilograma)
ro = 1.2     # Densidade do ar (kg/m**3)
Ca = 0.4     # Coeficiente de arrasto)
g = 9.8      # Aceleração da gravidade (m/s**2)
x0 = 0       # Posição incial do projétil eixo X)
y0 = 0       # Posição incial do projétil eixo Y)
A=50         # Área frontal do projétil
"""Equações diferenciais"""
def dxdt(Vx, t): # Distância percorrida no eixo X)    
    dxdt = Vx    
    return dxdt   

def dydt(Vy, t): # Distância percorrida no eixo Y
    dydt = Vy
    return dydt    
    
def dvxdt(fx,t): # Velocidade no eixo X
    dvxdt = fx/m   
    return dvxdt    

def dvydt(fy,t): # Velocidade no eixo Y
   dvydt = fy/m   
   return dvydt
  
    
def ResistX(v,vx,T):    # Força da resistência do ar no eixo X
    fx = -0.5*Ca*ro*A*v*vx
    return ResistX

T = linspace(0,250,251)    

Y = odeint(ResistX, A, T)