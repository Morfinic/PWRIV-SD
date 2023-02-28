from random import randint


class Node:
    def __init__(self, num):
        self.root = num
        self.left_sprout = None
        self.right_sprout = None

    def add(self, num):
        tmp = randint(0, 1)
        if tmp:
            if self.left_sprout is None:
                self.left_sprout = Node(num)
            else:
                self.left_sprout.add(num)
            return
        if self.right_sprout is None:
            self.right_sprout = Node(num)
        else:
            self.right_sprout.add(num)

    def print_tree(self, level=0):
        if self.left_sprout:
            self.left_sprout.print_tree(level + 1)
        print(' ' * 4 * level + str(self.root))
        if self.right_sprout:
            self.right_sprout.print_tree(level + 1)
