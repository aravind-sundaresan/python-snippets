# Question: How to reverse the words in a sentence?

def reverse_sentence_words(sentence):

	words = sentence.split()
	words.reverse()

	reversed_sentence = ' '.join(words)

	return reversed_sentence


def reverse_words_iterative(sentence):

	words = sentence.split()
	reversed_list = []

	i = len(words) - 1

	while i >= 0:
		reversed_list.append(words[i])
		i -= 1

	return (' '.join(reversed_list))


if __name__ == '__main__':
	sentence = "Think twice code once"

	reversed_sentence = reverse_sentence_words(sentence)
	print(reversed_sentence)

	reversed_sentence = reverse_words_iterative(sentence)
	print(reversed_sentence)