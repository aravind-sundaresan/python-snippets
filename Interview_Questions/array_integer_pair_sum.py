# Question: Find all Pairs Of Integers in an Array whose Sum is a Given Number

Read more: https://javarevisited.blogspot.com/2014/08/how-to-find-all-pairs-in-array-of-integers-whose-sum-equal-given-number-java.html#ixzz5HeNYXA1a
def integer_pair_sum(array, sum):

	dict = {}

	for i in range(len(array)):
		dict[i] = array[i]

	for i in range(len(array)):
		complement = sum - dict[i]
		if complement in dict.values():
			print(str(array[i]) + " " + str(complement))


if __name__ == '__main__':

	array = [2, 4, 3, 5, 7, 8, 9]
	required_sum = 8

	integer_pair_sum(array, required_sum)