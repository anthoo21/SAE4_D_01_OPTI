# test de méthodes, ...
# utile ?
# https://cpge.frama.io/fiches-cpge/Python/70-Derivee_Int%C3%A9grale/

from scipy.misc import derivative  # Fonction de dérivation
import numpy as np

x=[32,48,60,157,76,90]
y=[69.5,299,146,471.6,66,190]
a = 2.64 # valeur aléatoire
b = 3.53 # valeur aléatoire

# Fonction derivée à partir de a
def functionA():
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
def functionB():
    sommeX = 0
    sommeY = 0
    for i in range(len(x)):
        sommeX = x[i] + sommeX
    for i in range(len(x)):
        sommeY = y[i] + sommeY    
    deriver = 2*(a*sommeX+len(x)*b-sommeY)
    return deriver

print(functionA())
print(functionB())
