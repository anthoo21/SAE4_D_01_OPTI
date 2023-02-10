# test de méthodes, ...
# utile ?
# https://cpge.frama.io/fiches-cpge/Python/70-Derivee_Int%C3%A9grale/

import time

x=[32,48,60,157,76,90]
y=[69.5,299,146,471.6,66,190]

# Fonction derivée à partir de a
def functionA(a, b):
    sommeCarreX = 0
    sommeX = 0
    sommeXY = 0
    for i in range(len(x)):
        carre = x[i]**2
        sommeCarreX = carre + sommeCarreX
    for i in range(len(x)):
        sommeX = x[i] + sommeX
    for i in range(len(x)):
        sommeXY = x[i] * y[i] + sommeXY    
    deriver = 2*(a*sommeCarreX+b*sommeX-sommeXY)
    return deriver

# Fonction derivée à partir de b
def functionB(a, b):
    sommeX = 0
    sommeY = 0
    for i in range(len(x)):
        sommeX = x[i] + sommeX
    for i in range(len(x)):
        sommeY = y[i] + sommeY    
    deriver = 2*(a*sommeX+len(x)*b-sommeY)
    return deriver

def gradient(a, b, pas):
    isFini = True
    while(isFini):
        if(abs(functionA(a,b)) <= 0.001 and abs(functionB(a,b)) <= 0.001):
            isFini = False
        nouvA = functionA(a, b)
        nouvB = functionB(a, b)
        a = a-nouvA*pas
        b = b-nouvB*pas
    return a,b

a = 1
b = 1
pas = 0.00001
print(gradient(a, b ,pas))