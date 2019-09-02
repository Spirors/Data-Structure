class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        root = BSTNode(val)
    elif val < root.val:
        if root.left is None:
            root.left = BSTNode(val)
        else:
            insert(root.left, val)
    elif val > root.val:
        if root.right is None:
            root.right = BSTNode(val)
        else:
            insert(root.right, val)

def search(root, val):
    if root is None:
        return
    if val == root.val:
        return root
    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)

def preorder(root):
    if root is None:
        return
    print(root.val, end = " ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val, end = " ")

def delete(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = delete(root.left, val)
        return root
    if val > root.val:
        root.right = delete(root.right, val)
        return root
    if root.left is None:
        temp = root.right
        root = None
        return temp
    if root.right is None:
        temp = root.left
        root = None
        return temp
    else:
        parent = root.right
        curr = root.right
        while curr.left is not None:
            parent = curr
            curr = curr.left
        parent.left = curr.right
        root.val = curr.val
        curr = None
        return root

def main():
    print("init")
    root = BSTNode(2)
    insert(root, 4)
    insert(root, 3)
    insert(root, 1)
    insert(root, 9)
    insert(root, 7)
    insert(root, 5)
    print("inorder")
    inorder(root)
    print()
    print("search function check")
    node = search(root, 2)
    print(root.left.val, root.right.val)

    print("delete check")
    delete(root, 2)
    inorder(root)
    print()

if __name__ == '__main__':
	main()
