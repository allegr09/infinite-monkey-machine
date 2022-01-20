# -*- coding: utf-8 -*-

import numpy as np
import random
import enchant

def weighted_choice(objects, weights):
    weights = np.array(weights, dtype=np.float64)
    sum_of_weights = weights.sum()
    # standardization:
    np.multiply(weights, 1 / sum_of_weights, weights)
    weights = weights.cumsum()
    x = random.random()
    for i in range(len(weights)):
        if x < weights[i]:
            return objects[i]

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
weights = [0.072576422,0.01498825,0.021642121,0.037288185,0.111653038,0.020246161,0.017079351,0.059504,0.062585608,0.001143871,0.008941342,0.042053547,0.027575156,0.061093896,0.077800793,0.014311773,0.000920452,0.059153725,0.062109558,0.082409004,0.03230211,0.009188293,0.022433283,0.001230966,0.023240944,0.000423035]
d = enchant.Dict("en_US")

for i in range(0, 100000):
    word = ""
    for i in range(0, random.randint(3,8)):
        word = (word + weighted_choice(characters, weights))

    
   # if d.check(word) == True:
    print(word)
