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
        pass

    def __inorderPredecessor(self, node):
        pass
    
    def delete(self, item):
        pass

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

if __name__ == "__main__":
    main()