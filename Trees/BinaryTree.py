class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    '''
        Input format should be:
        Root, Left, right, left.left, left.right, right.left, right.right, etc
        If a node is None, put "N" instead of adding any number like -1, 0 etc.

        Example input:
        1 2 3 N 5 6 7 N N 

                     1
                 2        3
            N       5 6     7
    '''
    def __init__(self, items=[]):
        self.root = None
        if len(items) > 0:
            self.create(items)

    def create(self, items):
        if len(items) == 0:
            print("No items found to create Tree")
            return

        # Initialize a list as queue to use for level order traversal
        queue = []

        self.root = Node(int(items[0]))
        queue.append(self.root)

        # Initialize i with 1st index, as 0th index has already been processed
        i = 1
        while len(queue) > 0 and i < len(items):
            tempNode = queue.pop(0)

            # Update left child
            if i < len(items) and items[i] != 'N':
                lchild = Node(int(items[i]))
                tempNode.left = lchild
                queue.append(lchild)
            elif i >= len(items):
                break

            # Increment i after processing left child
            i += 1

            if i < len(items) and items[i] != 'N':
                rchild = Node(int(items[i]))
                tempNode.right = rchild
                queue.append(rchild)
            elif i >= len(items):
                break

            i += 1

    def preorder(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")

    def __str__(self):
        # Display tree in Preorder
        print("\nPreorder: ", end=" ")
        self.preorder(self.root)
        
        print("\nInorder: ", end=" ")
        self.inorder(self.root)
        
        print("\nPostorder: ", end=" ")
        self.postorder(self.root)
        return ""


        
def main():
    inputArray = input().split()
    tree = Tree(inputArray)
    print(tree)

if __name__ == '__main__':
    main()