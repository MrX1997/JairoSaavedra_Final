import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# Datos importados 
data=np.genfromtxt('datos_observacionales.dat',delimiter=' ')
t_obs=data[:,0]
x_obs=data[:,1]
y_obs=data[:,2]
z_obs=data[:,3]
sigma_obs=np.ones(len(t_obs))
obs=data[:,1:4]


#Modelo analitico
def funtion(state, t,sigma,rho,beta):
  x, y, z = state
  return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

def model(sigma,rho,beta):
    state0=[x_obs[0],y_obs[0],z_obs[0]]
    t=t_obs
    states=odeint(funtion,state0,t,args=(sigma, rho,beta))
    return states 
   
    
def loglikelihood(sigma,rho,beta):
    d = obs -  model(sigma,rho,beta)
    #print(d)
    d = -0.5 * np.sum(d**2)
    return d

#c=loglikelihood(1,5,4)
#print(c)

def logprior(sigma,rho,beta):
    param=[sigma,rho,beta]
    
    d = -0.5 *np.sum ((param)**2/(10.0)**2)
    return d

def divergence_loglikelihood(sigma,rho,beta):
    param=[sigma,rho,beta]
    n_param = len(param)
    div = np.ones(n_param)
    delta = 1E-5
    for i in range(n_param):
        delta_parameter = np.zeros(n_param)
        delta_parameter[i] = delta
        div[i] = loglikelihood(sigma + delta_parameter,rho + delta_parameter, beta + delta_parameter) 
        div[i] = div[i] - loglikelihood(sigma + delta_parameter,rho + delta_parameter, beta + delta_parameter)
        div[i] = div[i]/(2.0 * delta)
    return div

def hamiltonian(sigma,rho,beta, param_momentum):
    m = 100.0
    K = 0.5 * np.sum(param_momentum**2)/m
    V = -loglikelihood(sigma,rho,beta)     
    return K + V

def leapfrog_proposal(sigma,rho,beta, param_momentum):
    param=[sigma,rho,beta]
    N_steps = 5
    delta_t = 1E-2
    m = 100.0
    new_param = param.copy()
    new_param_momentum = param_momentum.copy()
    for i in range(N_steps):
        new_param_momentum = new_param_momentum + divergence_loglikelihood(sigma,rho,beta) * 0.5 * delta_t
        new_param = new_param + (new_param_momentum/m) * delta_t
        new_param_momentum = new_param_momentum + divergence_loglikelihood(sigma,rho,beta) * 0.5 * delta_t
    new_param_momentum = -new_param_momentum
    return new_param, new_param_momentum


def monte_carlo(N=5000):
    param = [np.random.random(3)]
    param_momentum = [np.random.normal(size=3)]
    for i in range(1,N):
        propuesta_param, propuesta_param_momentum = leapfrog_proposal(param[i-1],param[i-1],param[i-1], param_momentum[i-1])
        energy_new = hamiltonian(propuesta_param[0],propuesta_param[1],propuesta_param[2], propuesta_param_momentum)
        energy_old = hamiltonian(param[i-1],param[i-1], param[i-1], param_momentum[i-1])
   
        r = min(1,np.exp(-(energy_new - energy_old)))
        alpha = np.random.random()
        if(alpha<r):
            param.append(propuesta_param)
        else:
            param.append(param[i-1])
        param_momentum.append(np.random.normal(size=3))    

    param = np.array(param)
    return param

param_chain = monte_carlo(500)
n_param  = len(param_chain[0])
mejorparametro = []
for i in range(3):
    mejorparametro.append(np.mean(param_chain[:,i]))

plt.subplot(131)
plt.hist(param_chain[:,0],bins=100,density=True,label='Sigma')
plt.xlabel("Parametros")
plt.ylabel("Densidad")
plt.legend()
plt.subplot(132)
plt.hist(param_chain[:,1],bins=100,density=True,label='Sigma')
plt.xlabel("Parametros")
plt.ylabel("Densidad")
plt.legend()
plt.subplot(133)
plt.hist(param_chain[:,2],bins=100,density=True,label='Sigma')
plt.xlabel("Parametros")
plt.ylabel("Densidad")
plt.legend()

plt.savefig('MCH_figura1.pdf')
plt.close()



