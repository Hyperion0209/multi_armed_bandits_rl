"""
NOTE: You are only allowed to edit this file between the lines that say:
    # START EDITING HERE
    # END EDITING HERE

This file contains the MultiBanditsAlgo class. Here are the method details:
    - __init__(self, num_arms, horizon): This method is called when the class
        is instantiated. Here, you can add any other member variables that you
        need in your algorithm.
    
    - give_pull(self): This method is called when the algorithm needs to
        select an arm to pull. The method should return the index of the arm
        that it wants to pull (0-indexed).
    
    - get_reward(self, arm_index, set_pulled, reward): This method is called 
        just after the give_pull method. The method should update the 
        algorithm's internal state based on the arm that was pulled and the 
        reward that was received.
        (The value of arm_index is the same as the one returned by give_pull 
        but set_pulled is the set that is randomly chosen when the pull is 
        requested from the bandit instance.)
"""

import numpy as np

# START EDITING HERE
import math
# You can use this space to define any helper functions that you need
# END EDITING HERE


class MultiBanditsAlgo:
    def __init__(self, num_arms, horizon):
        # You can add any other variables you need here
        self.num_arms = num_arms
        self.horizon = horizon
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
        #raise NotImplementedError
        # END EDITING HERE
    
    def get_reward(self, arm_index, set_pulled, reward):
        # START EDITING HERE
        # print(set_pulled)
        # print("#####LNKJ######")
        if(reward > 0):
            self.successes[arm_index] += 1
        else:
            self.fails[arm_index] += 1
        #raise NotImplementedError
        # END EDITING HERE
# class MultiBanditsAlgo:
#     def __init__(self, num_arms, horizon):
#         # You can add any other variables you need here
#         self.num_arms = num_arms
#         self.horizon = horizon
#         # START EDITING HERE
#         self.curr_timestep = 0
#         self.once_0 = 0
#         self.once_1 = 0
#         self.counts_0 = np.full((num_arms,), 1e-5)
#         self.counts_1 = np.full((num_arms,), 1e-5)
#         self.initial_pulls = np.arange(num_arms)
#         np.random.shuffle(self.initial_pulls) 
#         self.values_0 = np.full((num_arms,), 1e-5)
#         self.values_1 = np.full((num_arms,), 1e-5)
#         self.ucb_arms_0 = np.zeros(num_arms)
#         self.ucb_arms_1 = np.zeros(num_arms)
#         self.actual_ucbs = np.zeros(num_arms)
#         # END EDITING HERE
    
#     def give_pull(self):
#         # START EDITING HERE
        # if self.once_0 + self.once_1 < 2*self.num_arms:
        #     if self.once_0 < self.once_1:
        #         return self.initial_pulls[self.once_0]
        #     else:
        #         return self.initial_pulls[self.once_1]
        
        # for i in range(self.num_arms):
        #     self.ucb_arms_0[i] = self.values_0[i] + math.sqrt((2*math.log(self.curr_timestep))/self.counts_0[i])
        #     self.ucb_arms_1[i] = self.values_1[i] + math.sqrt((2*math.log(self.curr_timestep))/self.counts_1[i])
        #     self.actual_ucbs[i] = (self.ucb_arms_0[i] + self.ucb_arms_1[i])*0.5
        # return np.argmax(self.actual_ucbs)
#         #raise NotImplementedError
#         # END EDITING HERE
    
#     def get_reward(self, arm_index, set_pulled, reward):
#         # START EDITING HERE
#         # print(set_pulled)
#         # print("#####LNKJ######")
        # if set_pulled == 0:
        #     n = self.counts_0[arm_index]
        #     # if n==1e-5:
        #     #     self.values_0[arm_index] = (self.values_0[arm_index]+reward)/2
        #     # else:
        #     #     self.values_0[arm_index] =  ((n- 1) / n) * self.values_0[arm_index] + (1 / n) * reward
        #     self.values_0[arm_index] =  ((n- 1) / n) * self.values_0[arm_index] + (1 / n) * reward
        #     self.once_0 += 1
        #     self.counts_0[arm_index] += 1
        # else:
        #     n = self.counts_1[arm_index]
        #     # if n==1e-5:
        #     #     self.values_1[arm_index] = (self.values_1[arm_index]+reward)/2
        #     # else:
        #     #     self.values_1[arm_index] =  ((n- 1) / n) * self.values_1[arm_index] + (1 / n) * reward
        #     self.values_1[arm_index] =  ((n- 1) / n) * self.values_1[arm_index] + (1 / n) * reward
        #     self.once_1 += 1
        #     self.counts_1[arm_index] += 1

        # self.curr_timestep += 1
#         #raise NotImplementedError
#         # END EDITING HERE

# class MultiBanditsAlgo:
#     def __init__(self, num_arms, horizon):
#         # You can add any other variables you need here
#         self.num_arms = num_arms
#         self.horizon = horizon
#         # START EDITING HERE
#         self.num_arms = num_arms
#         self.successes_0 = np.zeros(num_arms)
#         self.fails_0 = np.zeros(num_arms)
#         self.sampler_vals_0 = np.zeros(num_arms)
#         self.successes_1 = np.zeros(num_arms)
#         self.fails_1 = np.zeros(num_arms)
#         self.sampler_vals_1 = np.zeros(num_arms)
#         self.avg_sampler = np.zeros(num_arms)
#         # END EDITING HERE
    
#     def give_pull(self):
#         # START EDITING HERE
#         for i in range(self.num_arms):
#             alpha_0 = self.successes_0[i] + 1
#             beta_0 = self.fails_0[i] + 1
#             self.sampler_vals_0[i] = np.random.beta(alpha_0, beta_0)
#             alpha_1 = self.successes_1[i] + 1
#             beta_1 = self.fails_1[i] + 1
#             self.sampler_vals_1[i] = np.random.beta(alpha_1, beta_1)
#             self.avg_sampler = (self.sampler_vals_0[i] + self.sampler_vals_1[i])*0.5
#         return np.argmax(self.avg_sampler)
#         #raise NotImplementedError
#         # END EDITING HERE
    
#     def get_reward(self, arm_index, set_pulled, reward):
#         # START EDITING HERE
#         # print(set_pulled)
#         # print("#####LNKJ######")
#         if set_pulled == 0:
#             if(reward > 0):
#                 self.successes_0[arm_index] += 1
#             else:
#                 self.fails_0[arm_index] += 1
#         else:
#             if(reward > 0):
#                 self.successes_1[arm_index] += 1
#             else:
#                 self.fails_1[arm_index] += 1

#         #raise NotImplementedError
#         # END EDITING HERE

