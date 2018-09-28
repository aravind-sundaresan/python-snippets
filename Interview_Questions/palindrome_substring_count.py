def palindrome_check(substring):
    return (substring[::-1] == substring)

def palindrome_count(s):

    length = len(s)

    for i in range(3, length+1):
        for j in range(0, length-i+1):
            substring = s[j:j+i]

            if palindrome_check(substring) is True:
                print(substring)

    return

if __name__ == '__main__':
    palindrome_count("aaaaaa")
