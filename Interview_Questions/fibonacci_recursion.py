# Question: Print Fibonacci sequence using Recursion

def fibonacci_sequence(num):

	if num <= 1:
		return num

	return fibonacci_sequence(num - 1) + fibonacci_sequence(num - 2)

def fibonacci_sequence_memoization(num):

	if num <= 1:
		return num

	if fibonacci_array[num] != -1:
		return fibonacci_array[num]
	
	fibonacci_array[num] = fibonacci_sequence_memoization(num - 1) + fibonacci_sequence_memoization(num - 2)


n = 10
fibonacci_array = [-1] * n

if __name__ == '__main__':

	result = fibonacci_sequence(n)
	print(result)

	#fibonacci_sequence_memoization(n)