import numpy as np


class Bandit:
    
    def __init__(self, prob):
        self.p = prob
    
    def pull(self):
        return 1 if np.random.random() < self.p else 0

    
class Bandits:
    
    def __init__(self, probs):
        self.n = len(probs)
        self.bandits = [Bandit(p) for p in probs]
    
    def pull(self, action):
        return self.bandits[action].pull()