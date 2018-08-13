# Question: Write a program to check if a String contains another String

def substring_check(input_string, pattern):

	n = len(input_string)
	m = len(pattern)

	limit = n - m

	for i in range(0, limit + 1):
		for j in range(0, m):
			if input_string[i + j] != pattern[j]:
				break

			j += 1

		if j == m:
			print("Pattern found at position: " + str(i))


if __name__ == '__main__':
	input_string = "AABAACBBAACC"
	pattern = "BA"

	substring_check(input_string, pattern)