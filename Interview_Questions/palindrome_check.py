
def palindrome_check(input_string):

	for i in range(int(len(input_string) / 2)):
		
		if input_string[i] != input_string[len(input_string) - i - 1]:
			return False
	
	return True

if __name__ == '__main__':

	input_string = "malayalam"
	result = palindrome_check(input_string)	

	if result == True:
		print("Yes")
	else:
		print("No")