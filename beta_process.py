import numpy as np


class BetaHat:
    def __init__(self):
        self.mesure = dict()
        self.gamma = 0
    def add_one(self, w, p):
        if w in self.mesure:
            self.mesure[w] +=p
        else:
            self.mesure[w] = p
        self.gamma += p
    def add(self, omegas, ps):
        assert len(omegas) == len(ps)
        for i in range(len(omegas)):
            self.add_one(omegas[i], ps[i])
    def draw_bernouli_process(self):
        result = []
        for el in self.mesure:
            if np.random.random()<self.mesure[el]:
                result.append(el)
        return result

def b0_discrete(K, n = 10):
    return np.random.randint(0, n, size = K)/n

def b0_continuous(K):
    return np.random.random(size = K)


def step(c, n, B0, gamma, betahat):
    K = np.random.poisson(c * gamma /(c+n-1))
    omega =  B0(K)
    p = np.random.beta(1, c + n -1, size = K)
    betahat.add(omega, p)


def beta_process(B0, c, gamma, N = 2000):
    betahat = BetaHat()
    for n in range(1,N+1):
        step(c,n,B0, betahat)
    return betahat

def associated_bernoulli_process(B0, c, gamma, n = 20):
    B = beta_process(B0, c, gamma)
    result = []
    for i in range(n):
        result.append(B.draw_bernouli_process())
