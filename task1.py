"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the base Algorithm class that all algorithms should inherit
from. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)

We have implemented the epsilon-greedy algorithm for you. You can use it as a
reference for implementing your own algorithms.
"""

import numpy as np
import math
# Hint: math.log is much faster than np.log for scalars

class Algorithm:
    def __init__(self, num_arms, horizon):
        # print("hi")
        self.num_arms = num_arms
        self.horizon = horizon
    
    def give_pull(self):
        raise NotImplementedError
    
    def get_reward(self, arm_index, reward):
        raise NotImplementedError

# Example implementation of Epsilon Greedy algorithm
class Eps_Greedy(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # Extra member variables to keep track of the state
        self.eps = 0.1
        self.counts = np.zeros(num_arms)
        self.values = np.zeros(num_arms)
    
    def give_pull(self):
        if np.random.random() < self.eps:
            return np.random.randint(self.num_arms)
        else:
            return np.argmax(self.values)
    
    def get_reward(self, arm_index, reward):
        # print("hi")
        self.counts[arm_index] += 1
        n = self.counts[arm_index]
        value = self.values[arm_index]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.values[arm_index] = new_value

if __name__ == "__main__":
    eps = Eps_Greedy(40, 2)
    first = eps.give_pull()
    second = eps.give_pull()
    # print(eps.give_pull())
    print(first, second)
    print(eps.get_reward(eps.give_pull(), 5))
# START EDITING HERE
def kl_div(x, y):
    if x == 0:
        return math.log(1/(1-y))
    elif x==1:
        return math.log(1/y) 
    term1 = x*(math.log(x/y))
    term2 = (1-x)*math.log((1-x)/(1-y))
    return term1 + term2
# You can use this space to define any helper functions that you need
# END EDITING HERE

class UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        self.num_arms = num_arms
        self.curr_timestep = 0
        self.counts = np.zeros(num_arms)
        self.initial_pulls = np.arange(num_arms)
        np.random.shuffle(self.initial_pulls) 
        self.values = np.full((num_arms,), 1e-5)
        self.ucb_arms = np.zeros(num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        if self.curr_timestep < self.num_arms:
            return self.initial_pulls[self.curr_timestep]

        for i in range(self.num_arms):
            self.ucb_arms[i] = self.values[i] + math.sqrt((2*math.log(self.curr_timestep))/self.counts[i])
        
        return np.argmax(self.ucb_arms)
        # raise NotImplementedError
        # END EDITING HERE  
        
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        n = self.counts[arm_index]
        if n==0:
            self.values[arm_index] = (self.values[arm_index]+reward)/2
        else:
            self.values[arm_index] =  ((n- 1) / n) * self.values[arm_index] + (1 / n) * reward
        self.curr_timestep += 1
        self.counts[arm_index] += 1
        # raise NotImplementedError
        # END EDITING HERE


class KL_UCB(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.num_arms = num_arms
        self.curr_timestep = 0
        self.counts = np.zeros(num_arms)
        self.initial_pulls = np.arange(num_arms)
        np.random.shuffle(self.initial_pulls) 
        self.values = np.full((num_arms,), 1e-5)
        self.kl_ucb_arms = np.zeros(num_arms)


        # END EDITING HERE
    

    def give_pull(self):
    # START EDITING HERE
        if self.curr_timestep < self.num_arms:
            return self.initial_pulls[self.curr_timestep]
        
        for i in range(self.num_arms):
            p_a_t = self.values[i]
            lower = p_a_t
            upper = 1
            tolerance = 0.01

            while  (upper - lower)>tolerance:
                mid = (lower+upper)*0.5
                kl_term = kl_div(p_a_t, mid)
                if kl_term < math.log(self.curr_timestep)/self.counts[i] :
                    lower = mid
                else:
                    upper = mid
            self.kl_ucb_arms[i] = (lower+upper)*0.5
        
        return np.argmax(self.kl_ucb_arms)
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        n = self.counts[arm_index]
        if n==0:
            self.values[arm_index] = (self.values[arm_index]+reward)/2
        else:
            self.values[arm_index] =  ((n- 1) / n) * self.values[arm_index] + (1 / n) * reward

        self.counts[arm_index] += 1
        self.curr_timestep += 1
        # raise NotImplementedError
        # END EDITING HERE


class Thompson_Sampling(Algorithm):
    def __init__(self, num_arms, horizon):
        super().__init__(num_arms, horizon)
        # You can add any other variables you need here
        # START EDITING HERE
        self.num_arms = num_arms
        self.successes = np.zeros(num_arms)
        self.fails = np.zeros(num_arms)
        self.sampler_vals = np.zeros(num_arms)
        # END EDITING HERE
    
    def give_pull(self):
        # START EDITING HERE
        for i in range(self.num_arms):
            alpha = self.successes[i] + 1
            beta = self.fails[i] + 1
            self.sampler_vals[i] = np.random.beta(alpha, beta)
        return np.argmax(self.sampler_vals)
        # raise NotImplementedError
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        if(reward > 0):
            self.successes[arm_index] += 1
        else:
            self.fails[arm_index] += 1
        # raise NotImplementedError
        # END EDITING HERE
