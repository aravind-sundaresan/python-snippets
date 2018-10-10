'''
Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.

Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
'''

def subset_check(input_set, size, sum):

    if sum == 0:
        return True

    if size == 0 and sum != 0:
        return False

    if input_set[size - 1] > sum:
        return subset_check(input_set, size-1, sum)

    return subset_check(input_set, size-1, sum) or subset_check(input_set, size-1, sum-input_set[size - 1])

if __name__ == '__main__':
    input_set = [3, 34, 4, 12, 5, 2]
    sum = 20
    size = len(input_set)

    output = subset_check(input_set, size, sum)
    print(output)
