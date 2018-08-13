def binary_search(input_array, item, l, r):

	arr = input_array

	while l <= r:
		mid = int((l + r) / 2)

		if arr[mid] == item:
			return mid

		elif item > arr[mid]:
			l = mid + 1

		else:
			r = mid - 1

	return -1 


if __name__ == '__main__':
	input_array = [2, 3, 4, 10, 22, 40, 60, 75, 100]
	search_item = 40

	item_position = binary_search(input_array, search_item, 0, len(input_array)-1)
	print("Item found at index: " + str(item_position))