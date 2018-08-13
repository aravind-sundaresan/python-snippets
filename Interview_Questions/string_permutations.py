# Question: Print all permutations of a given string

def permute(input_string, l, r):

	a = list(input_string)

	if l == r:
		print(''.join(a)) 
		return

	for i in range(l, r):
		a[i], a[l] = a[l], a[i]
		permute(a, l + 1, r)
		a[i], a[l] = a[l], a[i]


if __name__ == '__main__':
	input_string = "ABC"

	permute(input_string, 0, len(input_string))