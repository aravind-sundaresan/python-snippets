'''
Problem:
Given a phonebook with entries,

2 -> abc
3 -> def
4 -> ghi
5 -> jkl
6 -> mno
7 -> pqrs
8 -> tuv
9 -> wxyz

For an input string: "23"
Output: [ad, ae, af, bd, be, bf, cd, ce, cf]
'''

def combination(digits):

    phone_dict = {2: ['a', 'b', 'c'], 3: ['d','e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    length_of_input = len(digits)

    if length_of_input == 0 or digits.isdigit() == False:
        return []

    if length_of_input == 1:
        return phone_dict[int(digits)]

    first_list = phone_dict[int(digits[0])]

    second_list = combination(digits[1:])
    digits = digits[1:]

    output = []
    for i in first_list:
        for j in second_list:
            output.append(i + j)

    return output

if __name__ == '__main__':
    output = combination("234")
    print(output)
