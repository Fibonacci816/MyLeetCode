class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        que = self.que1 if self.que1 else self.que2
        que.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.que1:
            n = len(self.que1)
            for i in range(n-1):
                self.que2.append(self.que1.pop(0))
            return self.que1.pop(0)
        else:
            n = len(self.que2)
            for i in range(n-1):
                self.que1.append(self.que2.pop(0))
            return self.que2.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        que = self.que1 if not self.que1 else self.que2
        res = self.pop()
        que.append(res)
        return res

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.que1) + len(self.que2) == 0


class MyStack2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que1 = []
        self.que2 = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.que2.append(x)
        while self.que1:
            self.que2.append(self.que1.pop(0))
        self.que1, self.que2 = self.que2, self.que1

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.que1.pop(0)


    def top(self) -> int:
        """
        Get the top element.
        """
        return self.que1[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.que1) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()