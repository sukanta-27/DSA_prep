from BinaryTree import Tree


def iterativePreorder(tree):
    if not tree.root:
        print("Tree is Empty")
        return

    stack = []

    current = tree.root
    while len(stack) > 0 or current:
        if current:
            print(current.data, end=" ")
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            current = current.right
    print()

def iterativeInorder(tree):
    if not tree.root:
        print("Tree is Empty")
        return

    stack = []
    current = tree.root

    while(current or len(stack) > 0):
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right

    print()

        
def iterativePostorderWith1Stack(root):
    pass

def iterativePostorderWith2Stacks(root):
    pass

    
def main():
    inputArray = input().split()
    tree = Tree(inputArray)
    
    print("Iterative Preorder: ")
    iterativePreorder(tree)

    print("Iterative Inorder: ")
    iterativeInorder(tree)
if __name__ == '__main__':
    main()