import numpy as np


class Bandit:
    """One-armed bandit"""
    
    def __init__(self, prob):
        """
        Parameters
        ----------
        prob : float
            probability of the jackpot
        """
        self.p = prob
    
    def pull(self):
        """Pull the lever of the bandit"""
        return 1 if np.random.random() < self.p else 0

    
class Bandits:
    """n-armed bandit"""
    
    def __init__(self, probs):
        """
        Parameters
        ----------
        probs : list
            list of probabilities of each bandit to jackpot
        """
        self.n = len(probs)
        self.bandits = [Bandit(p) for p in probs]
    
    def pull(self, action):
        """Pull the lever of the bandit
        Parameters
        ----------
        action : int
            the bandit id to pull
        """
        return self.bandits[action].pull()