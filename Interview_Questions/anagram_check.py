# Question: Check if 2 strings are Anagrams

import collections 

def sorted_check(first_string, second_string):
	if sorted(first_string) == sorted(second_string):
		print("Yes, these are anagrams")
	else:
		print("No, these aren't anagrams")


def counter_check(first_string, second_string):
	if collections.Counter(first_string) == collections.Counter(second_string):
		print("Yes, these are anagrams")
	else:
		print("No, these aren't anagrams")

if __name__ == '__main__':
	first_string = "bury"
	second_string = "ruby"

	sorted_check(first_string, second_string)
	counter_check(first_string, second_string)
