from binaryTree import Node
from random import randint
from stack import Stack

def main():
    # binTree = Node(0)
    # elemList = [randint(1, 15) for _ in range(40)]
    # for elem in elemList:
    #     binTree.add(elem)
    # binTree.print_tree()
    stack = Stack()
    stack.push(4)
    stack.push(6)
    stack.push(8)
    print(stack.peek())
    print(stack.is_empty())
    stack.print()
    stack.pop()
    stack.print()
    print(stack.size())

if __name__ == '__main__':
    main()
