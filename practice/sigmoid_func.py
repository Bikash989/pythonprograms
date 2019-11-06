import numpy as np
def sigmoid(z):
    '''
    :params: takes one np.array and returns the sigmoid of each values
    '''
    return (1 / (1 + np.exp(-z)))
    

li = list(range(10))
np_array = np.array(li)

print(sigmoid(np_array))


