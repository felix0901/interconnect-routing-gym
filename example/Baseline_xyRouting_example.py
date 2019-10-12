import random
import os
from collections import defaultdict, deque
import numpy as np
import matplotlib as mpl
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import csv
from src.icn_gym import *

## Global Parameters
actions = ["xy", "random_oblivious", "turn_model_oblivious", "turn_model_adaptive"]
a_size = len(actions) # space size of action
Q = defaultdict(lambda: np.zeros(a_size)) # Q-Table
dicts = defaultdict(list)
action_index = random.randint(0, 100)%2
action = actions[action_index]
iter_step = 6 # injection from 0.1 to 0.6
total_episodes = 1 # Game Playing times

epsilon = 1.0       # exploration rate
eps_min = 0.01
eps_decay = 0.999

### Plot Notebooks
time_history = []
rew_history = []
Q = defaultdict(lambda: np.zeros(a_size))

state = 0.1 # = Injection_rate as reset state env.reset()
# dicts = ICN_env(state, action) # ICM simulate()
for i in range(iter_step):
	state = (i+1)/10 # get next state
	action = "xy"
	dicts = ICN_env(state, action)
	
	# action = actions[random.randint(0, 100)%2]

rew_history.append(0) # Recording rewards



print('Q-Table = ', Q)

print('Reward = ', rew_history)

# print('Dicts = ',dicts)

csv_columns = ['average_flit_latency','average_packet_queueing_latency','average_flit_network_latency','average_flit_queueing_latency','packets_injected', 'average_packet_network_latency', 'average_hops',  'flits_injected', 'packets_received',  'flits_received', 'average_packet_latency']
csv_file = 'Inter_Connect_Networks/Tables/env_base_'+str(iter_step)+'_' +str(total_episodes)+ '.csv'

try:
	with open(csv_file, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(csv_columns)
		for i in range(len(dicts['average_flit_latency'])):
			writer.writerow([dicts[key][i] for key in csv_columns])
except IOError:
    print("I/O error")
# np.savetxt("Reward_history.csv", rew_history, delimiter=",")
### Plotting 

# print("Learning Performance")
mpl.rcdefaults()
mpl.rcParams.update({'font.size': 16})

fig, ax = plt.subplots(figsize=(10,4))
# plt.grid(True, linestyle='--')
plt.title('ICNs Learning')
# plt.plot(range(len(time_history)), time_history, label='Steps', marker="^", linestyle=":")#, color='red')
plt.plot(range(len(rew_history)), rew_history, label='Reward', marker="", linestyle="-")#, color='k')
plt.xlabel('Episodes')
plt.ylabel('Reward')
plt.savefig('Inter_Connect_Networks/Figures/shuffle_SARSA_'+str(iter_step)+'_'+str(total_episodes)+'_ICN.png', bbox_inches='tight')