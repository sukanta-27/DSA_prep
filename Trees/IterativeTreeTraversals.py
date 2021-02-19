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

        
def iterativePostorderWith1Stack(tree):
    if not tree.root:
        return []
    prev = None
    stack = [tree.root]
    result = []

    while stack:
        current = stack[-1]
        # Case 1
        if prev == None or prev.left == current or prev.right == current:

            if current.left:
                stack.append(current.left)
            elif current.right:
                stack.append(current.right)
            else:
                result.append(current.data)
                stack.pop()
        # Case 2
        elif prev == current.left:
            if current.right:
                stack.append(current.right)
        # Case 3
        else:
            result.append(current.data)
            stack.pop()
        
        prev = current
    
    print(*result)

def iterativePostorderWith2Stacks(tree):
    if not tree.root:
        return []
    
    stack1 = [tree.root]
    stack2 = []

    while stack1:
        current = stack1.pop()
        stack2.append(current.data)

        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    
    print(*stack2[::-1])


    
def main():
    inputArray = input().split()
    tree = Tree(inputArray)
    
    print("Iterative Preorder: ")
    iterativePreorder(tree)

    print("Iterative Inorder: ")
    iterativeInorder(tree)

    print("Iterative Postorder with 2 stacks: ")
    iterativePostorderWith2Stacks(tree)

    print("Iterative Postorder with 1 stack: ")
    iterativePostorderWith1Stack(tree)

if __name__ == '__main__':
    main()