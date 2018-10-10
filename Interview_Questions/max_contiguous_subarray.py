'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
'''
def max_subarray(input_array):

    length = len(input_array)
    sums = [0] * length
    sums[0] = input_array[0]

    for i in range(1, length):
        tmp = input_array[i] + sums[i - 1]

        if tmp > input_array[i]:
            sums[i] = tmp
        else:
            sums[i] = input_array[i]

    return max(sums)

if __name__ == '__main__':
    input_array =[-2,1,-3,4,-1,2,1,-5,4]
    largest_sum = max_subarray(input_array)
    print(largest_sum)
