# UDACITY: Intro to Deep Learning with PyTorch 
# Writing formula for Softmax Function

import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    totalSum = 0
    for i in expL:
        result.append(i*1.0/sumExpL)

    # Check if the probability sum is equal to 1.0 
    for single in result:
        totalSum = single + totalSum
    print("SUM: ", totalSum)
    
    # Return the probability list
    return result


print(softmax([-1,5,6]))