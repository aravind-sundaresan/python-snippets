# Question: How to remove duplicate characters from a String (maintain the order of characters)?

def remove_duplicates(input_string):

	char_count = {}

	for c in input_string:

		if c not in char_count:
			char_count[c] = 1
		else:
			char_count[c] += 1

	output_string = ""

	for c in char_count:
		output_string += c

	return output_string

if __name__ == '__main__':
	input_string = "bananas"

	output_string = remove_duplicates(input_string)
	print(output_string) 