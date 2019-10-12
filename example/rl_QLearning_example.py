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
max_state = iter_step/10
total_episodes = 15 # Game Playing times

epsilon = 1.0       # exploration rate
eps_min = 0.01
eps_decay = 0.999

### Plot Notebooks
time_history = []
rew_history = []
Q = defaultdict(lambda: np.zeros(a_size))

for i_episode in range(1, total_episodes+1):
	state = 0.1 # = Injection_rate as reset state env.reset()
	# state = np.reshape(state, [1, iter_step]) # iter_step = state_size
	rewardsum = 0
	# dicts = ICN_env(state, action) # ICM simulate()
	while True:# for i in range(iter_step):
		# if not done: # Env-Game on going
		# get epsilon-greedy action probabilities
		next_state = state + 0.1 # get next state
		policy_s = epsilon_greedy_probs(Q[next_state], i_episode)
		action_index = np.random.choice(np.arange(a_size), p = abs(policy_s))
		action = actions[action_index]
		dicts = ICN_env(state, action)
		reward = reward_f(dicts) # get reward from original action
		rewardsum += reward # Sum of Reward for this episode
		if epsilon > eps_min: epsilon *= eps_decay
		# pick next action A'
		# next_action_index = np.random.choice(np.arange(a_size), p=policy_s)
		# update TD estimate of Q
		Q[state][action_index] = update_Q(Q[state][action_index], np.max(Q[next_state]), \
													reward, .01, epsilon) 
		state = next_state
		if state == max_state:
			break
		# action = actions[random.randint(0, 100)%2]

	rew_history.append(rewardsum) # Recording rewards


print('Q-Table = ', Q)

print('Reward = ', rew_history)

### print('Dicts = ', dicts)

### Plotting 

# print("Learning Performance")
mpl.rcdefaults()
mpl.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=(10,4))
#plt.grid(True, linestyle='--')
plt.title('ICNs Learning')
# plt.plot(range(len(time_history)), time_history, label='Steps', marker="^", linestyle=":")#, color='red')
plt.plot(range(len(rew_history)), rew_history, label='Reward', marker="", linestyle="-")#, color='k')
plt.xlabel('Training Episodes')
plt.ylabel('Reward(-latency)')
plt.savefig('Inter_Connect_Networks/Figures/QL_'+str(iter_step)+'_'+str(total_episodes)+'_ICN.png', bbox_inches='tight')

csv_columns = ['average_flit_latency','average_packet_queueing_latency','packets_injected', 'average_packet_network_latency', 'average_hops',  'flits_injected', 'packets_received',  'flits_received', 'average_packet_latency']
csv_file = 'Inter_Connect_Networks/Tables/QL_'+str(iter_step)+'_'+str(total_episodes)+ '.csv'

try:
	with open(csv_file, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(csv_columns)
		for i in range(len(dicts['average_flit_latency'])):
			writer.writerow([dicts[key][i] for key,value in dicts.items()])
except IOError:
    print("I/O error")