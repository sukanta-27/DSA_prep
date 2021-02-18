class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BST:

    def __init__(self, items=[]):
        self.root = None
        if len(items) > 0:
            self.createBST(items)

    def createBST(self, items):
        for i in items:
            self.insert(i)

    def insert(self, item):
        if not self.root:
            self.root = Node(item)
            return
        
        current = self.root
        previous = None

        while current:
            previous = current
            if current.data == item:
                print("Item already exists in the BST")
                return
            elif current.data > item:
                current = current.left
            else:
                current = current.right
        
        if previous.data > item:
            previous.left = Node(item)
        else:
            previous.right = Node(item)
        
        return
            

    def __heightUtil(self, node):
        if not node:
            return 0
        
        x = self.__heightUtil(node.left)
        y = self.__heightUtil(node.right)

        return max(x,y)+1

    def height(self):
        """
            Assumption is that, empty tree has height = 0;
            Tree with 1 node has height = 1
        """
        return self.__heightUtil(self.root)
    
    def search(self, node, item):
        """
            @input: The root node.
            @input: The item that is needed to be searched
            @output: Node if item exists or else None
        """
        if not node:
            return None
        
        if node.data == item:
            return node
        elif node.data < item:
            return self.search(node.right, item)
        else:
            return self.search(node.left, item)

    def min(self):
        if not self.root:
            print("Empty tree")
        current = self.root
        min = None

        while current:
            min = current.data
            current = current.left
        return min

    def max(self):
        if not self.root:
            print("Empty tree")
        current = self.root
        max = None

        while current:
            max = current.data
            current = current.right
        return max

    def __inorderSuccessor(self, node):
        node = node.right
        while node.left:
            node = node.left
        return node.data

    def __inorderPredecessor(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node.data
    
    def delete(self, node, item):
        if not node:
            return None
        
        if node.data > item:
            node.left =  self.delete(node.left, item)
        elif node.data < item:
            node.right = self.delete(node.right, item)
        else:
            # Case 1: If node is a leaf node
            if not (node.left or node.right):
                node = None
            # Case 2: If there is a right child, replace with inorder successor
            elif node.right:
                node.data = self.__inorderSuccessor(node)
                node.right = self.delete(node.right, node.data)
            # Case 3: If there is no right child, replace with inorder predecessor
            else:
                node.data = self.__inorderPredecessor(node)
                node.left = self.delete(node.left, node.data)
        return node
        
    def __inorder(self, node):
        if not node:
            return
        
        self.__inorder(node.left)
        print(node.data, end=" ")
        self.__inorder(node.right)

    def __str__(self):

        print("Inorder: ")
        self.__inorder(self.root)
        return ""


def main():
    arr = list(map(int, input().split()))
    bst = BST(arr)
    print(bst)

    print("Height is: ", bst.height())
    print("Min is: ", bst.min())
    print("Max is: ", bst.max())
    print(bst.search(bst.root, 7))
    print(bst.search(bst.root, 3))
    
    t = int(input("********\n Enter the number of items you want to delete: "))
    for _ in range(t):
        x = int(input())
        bst.delete(bst.root, x)
        print(bst)

if __name__ == "__main__":
    main()