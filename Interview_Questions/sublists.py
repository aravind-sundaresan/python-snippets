def generate_sublists(input_list):

    sublists = [[]]

    length = len(input_list)

    for i in range(length + 1):
        for j in range(i + 1, length + 1):

            sublist = input_list[i:j]
            sublists.append(sublist)

    print(sublists)

if __name__ == '__main__':

    input_list = [1,2,3,4]
    generate_sublists(input_list)
