# -*- coding: utf-8 -*-
from scipy.integrate import odeint
from numpy import linspace
import matplotlib.pyplot as plt

#Lista de valores para tempo
T = linspace(0,50,1001)

#Parâmetros do sistema
m = 0.006   # Massa do projétil (kg) 0.006  0.01  0.003 
c = 18.37   # Coeficiente de amortecimento viscoso 18.37   32.46   18.37
k = 4      # Constante elástica da vibração   

#Condições iniciais do sistema
x0 = -0.1   # Amplitude incial (m)
v0 = 850    # Velocidade inicial (m/s)

#Função utilizada pelo ODEINT
X0 = [x0,v0]
def func2(X, t):
    dxdt = X[1]
    dvdt = (-k/m)*X[0] - (c/m)*X[1]
    return [dxdt, dvdt]

#Cálculo do ODEINT    
X = odeint(func2, X0, T)

#Lista de valores para tempo
T1 = linspace(0,50,1001)

#Parâmetros do sistema
m1 = 0.01   # Massa do projétil (kg) 0.006  0.01  0.003 
c1 = 25.65   # Coeficiente de amortecimento viscoso 18.37   32.46   18.37
k1 = 4      # Constante elástica da vibração   

#Condições iniciais do sistema
x01 = -0.1   # Amplitude incial (m)
v01 = 850    # Velocidade inicial (m/s)

#Função utilizada pelo ODEINT
X01 = [x01,v01]
def func2(X1, t1):
    dxdt1 = X1[1]
    dvdt1 = (-k1/m1)*X1[0] - (c1/m1)*X1[1]
    return [dxdt1, dvdt1]

#Cálculo do ODEINT    
X1 = odeint(func2, X01, T1)

#Lista de valores para tempo
T2 = linspace(0,50,1001)

#Parâmetros do sistema
m2 = 0.003   # Massa do projétil (kg) 0.006  0.01  0.003 
c2 = 12.81   # Coeficiente de amortecimento viscoso 18.37   32.46   18.37
k2 = 4      # Constante elástica da vibração   

#Condições iniciais do sistema
x02 = -0.1   # Amplitude incial (m)
v02 = 850    # Velocidade inicial (m/s)

#Função utilizada pelo ODEINT
X02 = [x02,v02]
def func2(X2, t2):
    dxdt = X2[1]
    dvdt = (-k2/m2)*X2[0] - (c2/m2)*X2[1]
    return [dxdt, dvdt]

#Cálculo do ODEINT    
X2 = odeint(func2, X02, T2)

#Plota 
plt.title("Sistema de amortecimento viscoso")
plt.xlabel('Distância (m)')
plt.ylabel('Vibração da munição (m)')
plt.plot(T, X[:,0],'b' )
plt.plot(T1,X1[:,0], "r")
plt.plot(T2,X2[:,0], 'g')
plt.show()

