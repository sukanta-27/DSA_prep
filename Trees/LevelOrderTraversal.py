from BinaryTree import Tree

def levelOrderTraversal(tree:Tree):
    if not tree.root:
        print("Tree is empty")
    
    queue = [tree.root]
    current = None

    while len(queue) > 0:
        current = queue.pop(0)
        print(current.data, end=" ")
        
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)
    
    print()
    return

def main():
    inputArray = input().split()
    tree = Tree(inputArray)
    levelOrderTraversal(tree)

if __name__ == '__main__':
    main()
