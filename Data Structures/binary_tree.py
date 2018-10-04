# Binary Tree Implementation

class BinaryTree:

    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def getRootValue(self):
        return self.root

    def setRootValue(self, value):
        self.root = value

    def insertLeft(self, newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.left = self.left
            self.left = tree

    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            tree = BinaryTree(newNode)
            tree.right = self.right
            self.right = tree

# Inorder traversal of the binary tree
def inorderTraversal(tree):
    if tree != None:
        inorderTraversal(tree.getLeftChild())
        print(tree.getRootValue())
        inorderTraversal(tree.getRightChild())

def preorderTraversal(tree):
    if tree != None:
        print(tree.getRootValue())
        preorderTraversal(tree.getLeftChild())
        preorderTraversal(tree.getRightChild())

def postorderTraversal(tree):
    if tree != None:
        postorderTraversal(tree.getLeftChild())
        postorderTraversal(tree.getRightChild())
        print(tree.getRootValue())

if __name__ == '__main__':
    tree = BinaryTree(1)
    tree.insertLeft(3)
    tree.insertRight(2)
    tree.insertLeft(4)
    #tree.getLeftChild().getLeftChild().insertLeft(10)
    #tree.getRightChild().insertLeft(5)
    #tree.getRightChild().insertRight(6)
    inorderTraversal(tree)
    preorderTraversal(tree)
    postorderTraversal(tree)
