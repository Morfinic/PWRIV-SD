class Stack:
    def __init__(self):
        self._stack = []
        self._stack_size: int = 0

    def push(self, item: int) -> None:
        self._stack.append(item)
        self._stack_size += 1

    def pop(self):
        if self._stack_size == 0:
            print("Stack is empty, returning None")
            return None
        tmp = self._stack[-1]
        del self._stack[-1]
        self._stack_size -= 1
        return tmp

    def size(self) -> int:
        return self._stack_size

    def is_empty(self) -> bool:
        return True if self._stack_size == 0 else False

    def peek(self):
        if self._stack_size == 0:
            print("Stack is empty, returning None")
            return None
        return self._stack[-1]

    def print(self):
        print(self._stack)
