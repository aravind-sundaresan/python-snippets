# Question: print the first non repeated character from a string

def non_repeated_character(test_string):

	char_count = {}

	for character in test_string:
		if character in char_count.keys():
			char_count[character] += 1
		else:
			char_count[character] = 1

	for key in char_count:
		if char_count[key] == 1:
			return key


if __name__ == '__main__':
	input_string = "geeksforgeeks"
	result = non_repeated_character(input_string)
	print(result)