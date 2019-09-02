class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self, head):
        self.head = head

    #O(n)
    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.val)
            curr = curr.next

    #O(n)
    def append(self, val):
        curr = self.head
        if curr is None:
            self.head = Node(val)
            return
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)

    #O(n)
    def remove(self, val):
        if self.head is None:
            return
        curr = self.head
        if val == self.head.val:
            self.head = curr.next
            return
        while curr is not None and curr.val != val:
            prev = curr
            curr = curr.next
        if curr is None:
            print("NOT FOUND")
            return
        prev.next = curr.next

def main():
    print("init")
    lst = SinglyLinkedList(None)
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.traverse()

    print("\nappending 10")
    lst.append(10)
    lst.traverse()

    print("\nRemoving 1")
    lst.remove(1)
    lst.traverse()

    print("\nRemoving 3")
    lst.remove(3)
    lst.traverse()

    print("\nRemoving 10")
    lst.remove(10)
    lst.traverse()

    print("\nremove -1")
    lst.remove(-1)

if __name__ == '__main__':
	main()
