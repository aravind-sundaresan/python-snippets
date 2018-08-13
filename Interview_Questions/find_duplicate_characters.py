# Question: Print the duplicate characters from a String

import collections

def duplicate_characters(test_string):

	char_count = {}

	for character in test_string:
		if character in char_count.keys():
			char_count[character] += 1
		else:
			char_count[character] = 1

	for key in char_count:
		if char_count[key] > 1:
			print(key)

def default_dict_duplicates(test_string):

	# Solution using the defaultdict collection, defaultdict adds a new key to the dictionary if it doesn't already exist 

	char_count = collections.defaultdict(int)
	for character in test_string:
		char_count[character] += 1

	for key in char_count:
		if char_count[key] > 1:
			print(key)


if __name__ == '__main__':
	input_string = "geeksforgeeks"
	default_dict_duplicates(input_string)