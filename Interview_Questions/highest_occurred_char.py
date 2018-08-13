# Question: How to return the highest occurred character in a String?

import collections

def char_frequency(test_string):

	char_count = {}

	for character in test_string:
		if character in char_count.keys():
			char_count[character] += 1
		else:
			char_count[character] = 1

	max_count, max_value = 0, 0

	for key in char_count:
		if char_count[key] > max_count:
			max_count = char_count[key]
			max_value = key

	return max_value


if __name__ == '__main__':
	input_string = "geeksforgeeks"
	result = char_frequency(input_string)
	print(result)