'''
Question: Write a function that takes a list L and returns a random sublist of size N of that list. Assume that the indexes must be in increasing order. That is, you cannot go backwards.

Example:

L = [1, 2, 3, 4, 5]
N = 3

The function should return one of these lists:

[1, 2, 3]
[1, 2, 4]
[1, 2, 5]
[1, 3, 4]
[1, 3, 5]
[1, 4, 5]
[2, 3, 4]
[2, 3, 5]
[2, 4, 5]
[3, 4, 5]

'''

import random

def generate_sublist(L, N):

    indices = [i for i in range(len(L))]
    random.shuffle(indices)
    indices = indices[:N]
    indices.sort()

    sublist = [L[j] for j  in indices]

    return sublist

if __name__ == '__main__':

    L = [1, 2, 3, 4, 5]
    N = 4

    sublist = generate_sublist(L, N)
    print(sublist)
