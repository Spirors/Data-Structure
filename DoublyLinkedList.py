class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        node = Node(val)
        while curr.next is not None:
            prev = curr
            curr = curr.next
        curr.next = node
        node.prev = curr

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
        curr.next.prev = prev
        prev.next = curr.next

def main():
    print("init")
    lst = DoublyLinkedList(None)
    lst.append(1)
    lst.append(2)
    lst.append(3)
    lst.traverse()

    print("\nchecking linkage")
    print(lst.head.prev) #None
    print(lst.head.next.prev.val)
    print(lst.head.next.val)
    print(lst.head.next.next.prev.val)
    print(lst.head.next.next.val)
    print(lst.head.next.next.next) #None

    print("\nremove 2")
    lst.remove(2)
    lst.traverse()
    print(lst.head.prev) #None
    print(lst.head.next.prev.val)
    print(lst.head.next.val)
    print(lst.head.next.next) #None

    print("\nremove -1")
    lst.remove(-1)

if __name__ == '__main__':
	main()
