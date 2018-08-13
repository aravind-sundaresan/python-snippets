class Node:

	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

class UnorderedList:

	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

	def size(self):
		count = 0
		current = self.head

		while current != None:
			count += 1
			current = current.getNext()

		return count

	def search(self, item):
		current = self.head
		count = 0

		while current != None:
			if current.getData() == item:
				print("Found")
				return count

			count += 1
			current = current.getNext()

	def traverse(self):
		current = self.head

		while current != None:
			print(current.getData())
			current = current.getNext()

	def remove(self, item):
		current = self.head
		previous = None

		while current != None:
			if current.getData() == item:

				# Check if the first item was removed
				if previous == None:
					self.head = current.getNext()

				else:
					previous.setNext(current.getNext())

			previous = current
			current = current.getNext()


if __name__ == '__main__':
	
	mylist = UnorderedList()

	mylist.add(20)
	mylist.add(31)
	mylist.add(10)
	mylist.add(26)

	#print(mylist.size())
	mylist.traverse()

	item = 10
	mylist.remove(item)
	print("List after removing " + str(item) + ":")
	mylist.traverse()
