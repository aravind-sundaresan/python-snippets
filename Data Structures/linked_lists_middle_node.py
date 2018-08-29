# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

from linked_lists import LinkedList

def brute_force(linked_list):

    current = linked_list.head
    length = 0

    while current != None:
        current = current.next_node
        length += 1

    current = linked_list.head

    for i in range(length // 2):
        current = current.next_node

    return current.data

def fast_and_slow_pointer(linked_list):

    fast = linked_list.head
    slow = linked_list.head

    while fast != None and fast.next_node != None:
        slow = slow.next_node
        fast = fast.next_node.next_node

    return slow.data

if __name__ == '__main__':

    linked_list = LinkedList()
    linked_list.insert_at_head(10)
    linked_list.insert_at_head(20)
    linked_list.insert_at_head(30)
    linked_list.insert_at_head(40)
    linked_list.insert_at_tail(50)
    linked_list.insert_at_tail(60)

    print("The linked list is as follows:")
    linked_list.traverse()

    middle_node_1 = brute_force(linked_list)
    print("Brute Force: The middle node is " + str(middle_node_1))

    middle_node_2 = fast_and_slow_pointer(linked_list)
    print("Fast and Slow pointer: The middle node is " + str(middle_node_2))
