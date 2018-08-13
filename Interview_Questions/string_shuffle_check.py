# Question: Check if a String is a valid shuffle of two Strings

def check_string_shuffle(a, b, c):

	i, j, k = 0, 0, 0

	for k in range(len(c)):
		
		if i < len(a) and c[k] == a[i]:
			i += 1

		elif j < len(b) and c[k] == b[j]:
			j += 1

		else:
			return False

	# If c has lesser number of characters
	if i != len(a) or j != len(b):
		return False

	return True


if __name__ == '__main__':

	a = "abc"
	b = "def"
	c = "dabecf"

	result = check_string_shuffle(a, b, c)
	print(result)