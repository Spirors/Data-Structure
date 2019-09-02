class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularLinkedList:
    def __init__(self, head):
        self.head = head

    #O(n)
    def traverse(self):
        curr = self.head
        while self.head is not None:
            print(curr.val)
            curr = curr.next
            if curr is self.head:
                break

    #O(n)
    def push(self, val):
        node = Node(val)
        curr = self.head
        node.next = self.head
        if self.head is not None:
            while curr.next is not self.head:
                curr = curr.next
            curr.next = node
        else:
            node.next = node
        self.head = node

    def remove(self, val):
        if self.head is None:
            return
        if val == self.head.val and self.head.next is self.head:
            self.head = None
            return
        curr = self.head
        if val == self.head.val:
            while curr.next is not self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = curr.next
            return
        while curr.next is not self.head and val != curr.next.val:
            curr = curr.next
        if val == curr.next.val:
            temp = curr.next
            curr.next = temp.next
        else:
            print("NOT FOUND")

def main():
    print("init")
    lst = CircularLinkedList(None)
    lst.push(3)
    lst.push(2)
    lst.push(1)
    lst.traverse()

    print("\nremove 2")
    lst.remove(2)
    lst.traverse()

    print("\nremove -1")
    lst.remove(-1)

if __name__ == '__main__':
	main()
