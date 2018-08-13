# Question: Find the Factorial of a number using Recursion

def factorial(number):

	if number <= 1:
		return number
				
	return (number * factorial(number - 1))

if __name__ == '__main__':
	
	result = factorial(5)
	print(result)