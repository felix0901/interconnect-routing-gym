# inconnect-routing-gym

ACM/IEEE NoCS, Oct. 2019
[Arxiv](https://arxiv.org/abs/1908.04484)

openai-gym style RL benchmark for interconnection network congestion control study

[CompArch - gem5/garnet tutorial](http://tusharkrishna.ece.gatech.edu/teaching/garnet_gt/)

[Running garnet](http://pwp.gatech.edu/ece-tushar/wp-content/uploads/sites/175/2019/01/Lab1.pdf)

<img src="https://github.com/huckiyang/inconnect-routing-gym/blob/master/ok_1.png" width="400">

### Environment Setup

```"shell"
$sudo apt-get install g++
$sudo apt-get install python
$sudo apt-get install python-dev
$sudo apt-get install swig
$sudo apt-get install zlib
$sudo apt-get install m4

```

### Downloading gem5

Official gem5 from [google git](https://gem5.googlesource.com/)

```
hg clone /nethome/tkrishna3/teaching/simulators/gem5/repo/gem5
```

- ``hg status`` shows what files have been modified in your repository

- ``hg diff`` shows a diff of the modified files.

### How to use it
Import the module in the src directry
* It provides integration with Garnet2.0 in gem5 with the custom-defined RL-alagirithm 
```"python"
from icn_gym import ICN_env as ir_gym
```
### Example
We provide examples of baseline (xy routing)
```
example/Baseline_xyRouting_example.py
```
We provides the example of three RL-alagorithms we present in the paper
```
example/rl_QLearning_example.py
example/rl_sarsa_example.py
example/rl_expected_sarsa_example.py
```
### Example of NoC statistics from Garnet2.0 in gem5
```
network_stats.txt
```
