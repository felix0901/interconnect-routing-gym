import random
import os
from collections import defaultdict, deque
import numpy as np
import matplotlib as mpl
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import csv
from icn_gym import *

## Global Parameters
actions = ["xy", "random_oblivious", "turn_model_oblivious", "turn_model_adaptive"]
a_size = len(actions) # space size of action
Q = defaultdict(lambda: np.zeros(a_size)) # Q-Table
dicts = defaultdict(list)
action_index = random.randint(0, 100)%2
action = actions[action_index]
iter_step = 6 # injection from 0.1 to 0.6
total_episodes = 15 # Game Playing times

epsilon = 1.0       # exploration rate
eps_min = 0.01
eps_decay = 0.999

### Plot Notebooks
time_history = []
rew_history = []
Q = defaultdict(lambda: np.zeros(a_size))

for i_episode in range(total_episodes):
	state = 0.1 # = Injection_rate as reset state env.reset()
	# state = np.reshape(int(100*state), [1, iter_step]) # iter_step = state_size
	policy_s = epsilon_greedy_probs(Q[state], i_episode)
	action_index = np.random.choice(np.arange(a_size), p = abs(policy_s))
	action = actions[action_index]
	rewardsum = 0
	# dicts = ICN_env(state, action) # ICM simulate()
	for i in range(iter_step):
		next_state = state + 0.1 # get next state
		dicts = ICN_env(state, action)
		reward = reward_f(dicts) # get reward from original action
		rewardsum += reward # Sum of Reward for this episode
		if epsilon > eps_min: epsilon *= eps_decay
		# if not done: # Env-Game on going
		# get epsilon-greedy action probabilities
		policy_s = epsilon_greedy_probs(Q[next_state], i_episode)
		# pick next action A'
		next_action_index = np.random.choice(np.arange(a_size), p=policy_s)
		# update TD estimate of Q
		Q[state][action_index] = update_Q(Q[state][action_index], np.dot(Q[next_state], policy_s), \
												reward, .01, epsilon)
		action_index = next_action_index
		action = actions[action_index] # get next action
		state = next_state
		# action = actions[random.randint(0, 100)%2]

	rew_history.append(rewardsum) # Recording rewards


print('Q-Table:', Q)

print('Reward:', rew_history)

csv_columns = ['average_flit_latency','average_packet_queueing_latency','average_flit_network_latency','average_flit_queueing_latency','packets_injected', 'average_packet_network_latency', 'average_hops',  'flits_injected', 'packets_received',  'flits_received', 'average_packet_latency']
csv_file = 'Inter_Connect_Networks/Tables/ESARSA_'+str(iter_step)+'_'+str(total_episodes)+'.csv'

try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dicts:
            writer.writerow(data)
except IOError:
    print("I/O error")
# np.savetxt("Reward_history.csv", rew_history, delimiter=",")

### Plotting 

# print("Learning Performance")
mpl.rcdefaults()
mpl.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=(10,4))
#plt.grid(True, linestyle='--')
plt.title('ICNs Learning')
# plt.plot(range(len(time_history)), time_history, label='Steps', marker="^", linestyle=":")#, color='red')
plt.plot(range(len(rew_history)), rew_history, label='Reward', marker="", linestyle="-")#, color='k')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.savefig('Inter_Connect_Networks/Figures/ESARSA_'+str(iter_step)+'_'+str(total_episodes)+'_ICN.png', bbox_inches='tight')