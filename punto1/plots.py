import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return (1.0/np.sqrt(2*np.pi))*np.exp(-x*x/2)

def B(proms):
    rta = (proms - proms.mean())**2
    return 1000/(len(proms)-1) *rta.sum()

def W(desvs):
    rta = desvs**2
    return rta.sum() / len(desvs)

