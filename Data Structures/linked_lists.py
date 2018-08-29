# Class to represent an individual node in the linked list
class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self,new_next):
        self.next_node = new_next

# Class to represent the linked list and it's operations
class LinkedList:

    def __init__(self, head=None):
        self.head = head

    # Function to insert an element at the beginning of the list
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Function to insert an element at the end of the list
    def insert_at_tail(self, data):
        current = self.head
        previous = None

        while current != None:
            previous = current
            current = current.get_next()

        new_node = Node(data)
        previous.set_next(new_node)

    # Function to insert an element at a particular index in the list
    def insert_at_index(self, index, data):
        current = self.head
        previous = None
        list_index = 0

        # Beginning of the list
        if index == 0:
            self.insert_at_head(data)

        # End of the list
        if index == self.size():
            self.insert_at_tail(data)

        while current != None:
            if list_index == index:

                new_node = Node(data)
                previous.set_next(new_node)
                new_node.set_next(current)

            previous = current
            current = current.get_next()
            list_index += 1

        return -1

    # Function to obtain the size of the list
    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.get_next()

        return count

    # Function to search for an element in the list
    def search(self, data):
        current = self.head

        while current != None:
            if current.get_data() == data:
                return 0

            current = current.get_next()

        # If the element is not found in the list
        if current == None:
            return -1

    # Function to delete an element from the list
    def delete(self, data):
        current = self.head
        previous = None

        while current != None:
            if current.get_data() == data:
                # Check if the first element was deleted
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())

                return 0

            previous = current
            current = current.get_next()

        return -1

    # Function to delete an element at a particular index from the list
    def delete_at_index(self, index):
        current = self.head
        previous = None
        list_index = 0

        while current != None:
            if list_index == index:
                if previous == None:
                    self.head = current.get_next()
                else:
                    previous.set_next(current.get_next())

                return 0

            previous = current
            current = current.get_next()
            list_index += 1

        return -1

    # Funciton to traverse the linked list
    def traverse(self):
        current = self.head

        while current != None:
            print(current.get_data())
            current = current.get_next()

    # Function to get the value of the index-th node in the linked list
    def get(self, index):
        current = self.head
        list_index = 0

        while current != None:
            if list_index == index:
                return current.get_data()

            current = current.get_next()
            list_index += 1

        return -1

if __name__ == '__main__':

    linked_list = LinkedList()

    linked_list.insert_at_head(10)
    linked_list.insert_at_head(20)
    linked_list.insert_at_tail(30)

    print("Size of the list is " + str(linked_list.size()))

    linked_list.delete(20)
    print("Size of the list after deleting an element is " + str(linked_list.size()))

    linked_list.insert_at_tail(40)
    linked_list.insert_at_head(20)
    linked_list.insert_at_tail(50)
    linked_list.insert_at_index(5, 55)
    linked_list.delete_at_index(4)
    print("The updated list is as follows: ")
    linked_list.traverse()

    index = 3
    print("Element at index " + str(index) + " is " + str(linked_list.get(index)))
