# Question: Program to sort strings based on their length

def sort_strings(string_list):

	n = len(string_list)

	for i in range(n):
		for j in range(n - i - 1):
			if( len(string_list[j + 1]) < len(string_list[j]) ):
				string_list[j], string_list[j + 1] = string_list[j + 1], string_list[j]

	return string_list
	

if __name__ == '__main__':
	
	string_list = ["hello", "there", "!", "how", "are", "you", "doing", "?"]

	sorted_list = sort_strings(string_list)
	print(sorted_list)