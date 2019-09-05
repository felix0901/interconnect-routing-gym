# inconnect-routing-gym

- work in progress - code will release in the Sep. [Arxiv](https://arxiv.org/abs/1908.04484)

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

```
hg clone /nethome/tkrishna3/teaching/simulators/gem5/repo/gem5
```

- ``hg status`` shows what files have been modified in your repository

- ``hg diff`` shows a diff of the modified files.

```"python"
import inconnect_routing_gym as ir-gym

```
