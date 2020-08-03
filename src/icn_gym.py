import random
import os
from collections import defaultdict, deque
import numpy as np
import matplotlib as mpl
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import csv
# import time as ti
# import pandas as pd

def update_Q(Qsa, Qsa_next, reward, alpha = 0.01, gamma = 1.0):
	""" updates the action-value function estimate using the most recent time step """
	return Qsa + (alpha * (reward + (gamma * Qsa_next) - Qsa))

def epsilon_greedy_probs( Q_s, i_episode, eps = None):
	""" obtains the action probabilities corresponding to epsilon-greedy policy """
	epsilon = 1.0 / (i_episode+1)
	if eps is not None:
		epsilon = eps
	policy_s = np.ones(a_size) * epsilon / a_size
	policy_s[np.argmax(Q_s)] = 1 - epsilon + (epsilon / a_size)
	return abs(policy_s)

def reward_f(d):
	latency = float(d["average_packet_latency"][-1])
	return -round(latency,2) # minimize latency

def ICN_env(injrate, action): # injrate = state
	os_command = "./build/Garnet_standalone/gem5.opt configs/example/garnet_synth_traffic.py --network=garnet2.0 --num-cpus=64 --num-dirs=64 --topology=Mesh --mesh-rows=8 --sim-cycles=20000 --inj-vnet=0 --injectionrate={:f} --synthetic=shuffle --routing-algorithm={}".format(injrate, action)
	os.system(os_command)
	os_command2 = "./my_scripts/extract_network_stats.sh"
	os.system(os_command2)
	with open("./network_stats.txt", "r") as fd:
		for line in fd:
			line_ele = line.split(" ")
			if len(line_ele) > 3:
				my_line = line_ele
				key = my_line[0]
				val = my_line[2]
				dicts[key].append(val)
	# print(dicts)

	return dicts
