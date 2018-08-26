import numpy as np
from enum import Enum


class Action (Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3


gridmap = [[0,0,0,0],[0,1,2,5],[1,2,3,6],[2,3,3,7],
           [4,0,5,8],[4,1,6,9],[5,2,7,10],[6,3,7,11],
           [8,4,9,12], [8,5,10,13], [9,6,11,14], [10,7,11,15],
           [12,8,13,12], [12,9,14,13], [13,10,15,14],[0,0,0,0]]

v_k = np.array([[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]])

policy = [['terminated'], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],
          [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],
          [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4],
          [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], ['terminated']]

Theta = 0.01

class IterationType (Enum):
    POLICY = 1
    VALUE = 2

def policy_iteration():
    y = 1

def value_iteration():
    x = 1

def step(state, action):
    reward = -1
    return reward, gridmap[state][action]

if __name__ == '__main__':

    Type = IterationType.POLICY

    if(Type == IterationType.POLICY):
        policy_iteration()
    else:
        value_iteration()
