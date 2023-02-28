from binaryTree import Node
from random import randint

def main():
    binTree = Node(0)
    elemList = [randint(1, 15) for _ in range(10)]
    for elem in elemList:
        binTree.add(elem)
    binTree.print_tree()

if __name__ == '__main__':
    main()
