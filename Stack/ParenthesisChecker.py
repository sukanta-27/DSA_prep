def checkParenthesis(expression):
    stack = []
    map = {
        ")":"(",
        "}":"{",
        "]":"["
    }
    s = set(['(', ')', '{', '}', '[', ']'])

    for i in expression:
        # print(stack)
        if i in s:
            if i in map:
                if len(stack) == 0 or stack[-1] != map[i]:
                    return False
                else:
                    stack.pop()

            else:
                stack.append(i)
    
    return len(stack) == 0

def main():
    t = int(input("Enter the number of test cases: "))
    while(t > 0):
        s = input("Enter the expression: ")
        print(checkParenthesis(s))
        t -= 1

if __name__ == "__main__":
    main()