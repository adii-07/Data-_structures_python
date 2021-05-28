# Making Node class to store each data and address of next element
class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


# Making Linked list class to define all operations
class LinkedList:
    """docstring for LinkedList"""

    def __init__(self):
        self.head = None

    # function to print the linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            ll_str = ''

            while itr:
                ll_str += str(itr.data) + '-->' if itr.nxt else str(itr.data)
                itr = itr.nxt
            print(ll_str)

    # function for getting length of linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.nxt
        return count

    # function for appending new element to the linked list
    def append(self, data):
        if self.head is None:
            self.head = Node(data, None)
        else:
            itr = self.head
            while itr.nxt:
                itr = itr.nxt

            itr.nxt = Node(data, None)

    # function to insert a list of elements using append function
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.append(data)

    # function to insert element at specific position
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index. Linked list has {} elements".format(self.get_length))

        elif index == 0:
            node = Node(data.head)
            self.head = node

        else:
            count = 0
            itr = self.head
            while itr.nxt:

                if count == index - 1:
                    node = Node(data, itr.nxt)
                    itr.nxt = node
                    break
                itr = itr.nxt
                count += 1

    # function to remove any element at given index
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index. Linked list has {} elements".format(self.get_length))
        elif index == 0:
            self.head = self.head.nxt
        else:
            count = 0
            itr = self.head
            while itr.nxt:
                if count == index - 1:
                    itr.nxt = itr.nxt.nxt
                    break

                itr = itr.nxt
                count += 1

    # function to pop element
    def pop(self):
        if self.head is None:
            print("Linked list is empty")
        elif self.get_length() == 1:
            self.head = None
        else:
            itr = self.head

            while itr.nxt.nxt:
                itr = itr.nxt
            itr.nxt = None


# main function
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values([10, 20, 40, 60])  # inserting list of elements in linked list
    ll.print()  # printing linked list
    ll.insert_at(2, 30)  # inserting element at given index
    ll.print()
    ll.remove_at(4)  # removing element at given index
    ll.print()
    ll.append(50)  # appending element at the end
    ll.print()
    ll.pop()
    ll.print()
    ll.pop()
    ll.print()
    ll.pop()
    ll.print()
    ll.pop()
    ll.print()
    ll.pop()
    ll.print()

# Output
# 10-->20-->40-->60
# 10-->20-->30-->40-->60
# 10-->20-->30-->40
# 10-->20-->30-->40-->50
# 10-->20-->30-->40
# 10-->20-->30
# 10-->20
# 10
# Linked list is empty
