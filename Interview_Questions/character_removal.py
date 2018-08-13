# Question: Write a program to remove a given character from a string

def remove_character(input_string, character):

	output_string = ""

	for c in input_string:
		if c != character:
			output_string += c

	return output_string


if __name__ == '__main__':
	input_string = "geeksforgeeks"
	input_character = 'e'

	output_string = remove_character(input_string, input_character)
	print(output_string)