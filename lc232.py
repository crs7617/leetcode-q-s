class MyQueue:

    def __init__(self):
        self.myStack = []

    def push(self, x: int) -> None:
        self.myStack.append(x)

    def pop(self) -> int:
        return self.myStack.pop(0)

    def peek(self) -> int:
        return self.myStack[0]

    def empty(self) -> bool:
        return not self.myStack
