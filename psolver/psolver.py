
__author__ = "aravind"

import sys

#Generate all possible arithmetic expressions (without parentheses) with the given digits
def generate_expressions(digit_list):
    queue = []
    for digit in digit_list:
        tmp = []
        while queue:
            previous = queue.pop(0)
            tmp.append(previous + '+' + str(digit))
            tmp.append(previous + '-' + str(digit))
            tmp.append(previous + '*' + str(digit))
            tmp.append(previous + '/' + str(digit))
        if tmp == []:
          	tmp.append(str(digit))
        queue = tmp[:]
    yield queue


#Add parentheses to each arithmetic expression
def balanced_parentheses(arithmetic_expression):
    if arithmetic_expression.isdigit():
        yield arithmetic_expression
    else:
        i = 0
        while i < len(arithmetic_expression)-1:
            while i < len(arithmetic_expression) and arithmetic_expression[i].isdigit():
                i += 1
            if i < len(arithmetic_expression) - 1:
                for left in balanced_parentheses(arithmetic_expression[:i]):
                    for right in balanced_parentheses(arithmetic_expression[i+1:]):
                        yield '({}{}{})'.format(left, arithmetic_expression[i], right)
            i += 1

 
#Find the smallest number that cannot be generated from the given numbers           
def find_smallest_number(expressions, c, d):

	expression_results = []
	unique_results = set()

	for expression in expressions:
		for i in expression:
			if "*" not in i and "/" not in i:
				try:
					result = eval(i)
					if result in unique_results or result<1 or result!=int(result):
						continue
					else:
						unique_results.add(result)
						expression_results.append([i, eval(i)])
				except ZeroDivisionError:
					continue
			else:

				trees = balanced_parentheses(i)
				for tree in trees:
					try:
						result = eval(tree)
						if result in unique_results or result<1 or result!=int(result):
							continue
						else:
							unique_results.add(result)
							expression_results.append([tree, eval(tree)])
					except ZeroDivisionError:
						continue

	unique_results = sorted(unique_results)
	for i in range(1, unique_results[-1]):
		if i not in unique_results:
			return i
	

#Find the expression that generates the target value
def find_target(expressions, c, d, t):

	expression_results = []
	unique_results = set()

	for expression in expressions:
		for i in expression:
			if "*" not in i and "/" not in i:
				try:
					result = eval(i)
					if result==t:
						print(str(t) + " can be computed in " + str(c) + " " + str(d) + "s")
						print("here is how: " + str(i) + " = " + str(result))
						return 0		
				except ZeroDivisionError:
					continue
			else:

				trees = balanced_parentheses(i)
				for tree in trees:
					try:
						result = eval(tree)
						if result==t:
							print(str(t) + " can be computed in " + str(c) + " " + str(d) + "s")
							print("here is how: float" + str(tree) + " = " + str(result))
							return 0		
					except ZeroDivisionError:
						continue
	print(str(t) + " cannot be computed in " + str(c) + " " + str(d) + "s")

def main():

	if len(sys.argv)!=5 and len(sys.argv)!=7:
		print("Usage: python3 psolver.py -c -d -t")
		

	c = int(sys.argv[2])
	d = int(sys.argv[4])

	digits = []
	for i in range(c):
		digits.append(d)

	
	if len(sys.argv)==5:

		expressions = generate_expressions(digits)
		smallest_number_not_possible = find_smallest_number(expressions, c, d)
		print(str(smallest_number_not_possible) + " cannot be computed in " + str(c) + " " + str(d) + "s")


	elif len(sys.argv)==7:
		t = int(sys.argv[6])
		expressions = generate_expressions(digits)
		find_target(expressions, c, d, t)


if __name__ == '__main__':
	main()
			
