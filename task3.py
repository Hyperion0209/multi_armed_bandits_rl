"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the FaultyBanditsAlgo class. Here are the method details:
    - __init__(self, num_arms, horizon, fault): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, reward): This method is called just after the 
        give_pull method. The method should update the algorithm's internal
        state based on the arm that was pulled and the reward that was received.
        (The value of arm_index is the same as the one returned by give_pull.)
"""

import numpy as np
import math

# START EDITING HERE
# You can use this space to define any helper functions that you need
import math
def kl_div(x, y):
    if x == 0:
        return math.log(1/(1-y))
    elif x==1:
        return math.log(1/y) 
    term1 = x*(math.log(x/y))
    term2 = (1-x)*math.log((1-x)/(1-y))
    return term1 + term2
# END EDITING HERE

class FaultyBanditsAlgo:
    def __init__(self, num_arms, horizon, fault):
        # You can add any other variables you need here
        self.num_arms = num_arms
        self.horizon = horizon
        self.fault = fault # probability that the bandit returns a faulty pull
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
        # for i in range(self.num_arms):
        #     p_a_t = self.values[i]
        #     lower = p_a_t
        #     upper = 1
        #     tolerance = 0.01

        #     while  (upper - lower)>tolerance:
        #         mid = (lower+upper)*0.5
        #         kl_term = kl_div(p_a_t, mid)
        #         if kl_term < math.log(self.curr_timestep)/self.counts[i] :
        #             lower = mid
        #         else:
        #             upper = mid
        #     self.kl_ucb_arms[i] = (lower+upper)*0.5
        
        # return np.argmax(self.kl_ucb_arms)

        # if np.random.random() < self.eps:
        #     return np.random.randint(self.num_arms)
        # for i in range(self.num_arms):
        #     n = self.counts[i]
        #     if n == 0:
        #         n= 1e-5
        #     self.mod_ucb_arms[i] = self.values[i] + math.sqrt((2*math.log(self.horizon))/n)
        
        # return np.argmax(self.mod_ucb_arms)
        # raise NotImplementedError
        # END EDITING HERE
    
    def get_reward(self, arm_index, reward):
        # START EDITING HERE
        if(reward > 0):
            self.successes[arm_index] += 1
        else:
            self.fails[arm_index] += 1
        # fault_or_not = np.random.choice([0,1], p=[self.fault, self.not_fault])
        # n = self.counts[arm_index]
        # self.counts[arm_index] += 1
        # self.fails += 1 - fault_or_not
        # if n!= 0:
        #     self.values = self.fails/n
        # else:
        #     self.values = self.fails


        # raise NotImplementedError
        #END EDITING HERE
        
# class FaultyBanditsAlgo:
#     def __init__(self, num_arms, horizon, fault):
#         # You can add any other variables you need here
#         self.num_arms = num_arms
#         self.horizon = horizon
#         self.fault = fault # probability that the bandit returns a faulty pull
#         # START EDITING HERE
#         self.eps = 0.1
#         self.not_fault = 1-self.fault
#         self.curr_timestep = 0
#         self.good_ones = 0
#         self.counts = np.zeros(num_arms)
#         self.initial_pulls = np.arange(num_arms)
#         np.random.shuffle(self.initial_pulls) 
#         self.values = np.full((num_arms,), 1e-5)
#         self.fails = np.zeros(num_arms)
#         self.ucb_arms = np.zeros(num_arms)
#         self.kl_ucb_arms = np.zeros(num_arms)
#         self.mod_ucb_arms = np.zeros(num_arms)
#         # END EDITING HERE
    
#     def give_pull(self):
#         # START EDITING HERE
#         if self.good_ones < self.num_arms:
#             return self.initial_pulls[self.good_ones]
#         for i in range(self.num_arms):
#             self.ucb_arms[i] = self.values[i] + math.sqrt((2*math.log(self.curr_timestep))/self.counts[i])
#         return np.argmax(self.ucb_arms)
#         # for i in range(self.num_arms):
#         #     p_a_t = self.values[i]
#         #     lower = p_a_t
#         #     upper = 1
#         #     tolerance = 0.01

#         #     while  (upper - lower)>tolerance:
#         #         mid = (lower+upper)*0.5
#         #         kl_term = kl_div(p_a_t, mid)
#         #         if kl_term < math.log(self.curr_timestep)/self.counts[i] :
#         #             lower = mid
#         #         else:
#         #             upper = mid
#         #     self.kl_ucb_arms[i] = (lower+upper)*0.5
        
#         # return np.argmax(self.kl_ucb_arms)

#         # if np.random.random() < self.eps:
#         #     return np.random.randint(self.num_arms)
#         # for i in range(self.num_arms):
#         #     n = self.counts[i]
#         #     if n == 0:
#         #         n= 1e-5
#         #     self.mod_ucb_arms[i] = self.values[i] + math.sqrt((2*math.log(self.horizon))/n)
        
#         # return np.argmax(self.mod_ucb_arms)
#         # raise NotImplementedError
#         # END EDITING HERE
    
#     def get_reward(self, arm_index, reward):
#         # START EDITING HERE
#         fault_or_not = np.random.choice([0,1], p=[self.fault, self.not_fault])
#         #0==fault, 1==not fault
#         if fault_or_not:
#             n = self.counts[arm_index]
#             if n==0:
#                 self.values[arm_index] = (self.values[arm_index]+reward)/2
#             else:
#                 self.values[arm_index] =  ((n- 1) / n) * self.values[arm_index] + (1 / n) * reward
#             self.good_ones += 1
#             self.counts[arm_index] += 1
#         self.curr_timestep += 1
#         # fault_or_not = np.random.choice([0,1], p=[self.fault, self.not_fault])
#         # n = self.counts[arm_index]
#         # self.counts[arm_index] += 1
#         # self.fails += 1 - fault_or_not
#         # if n!= 0:
#         #     self.values = self.fails/n
#         # else:
#         #     self.values = self.fails


#         # raise NotImplementedError
#         #END EDITING HERE





