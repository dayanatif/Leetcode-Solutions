class MyStack:

    def __init__(self):
        self.q1 =[]
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while self.q1:
            x = self.q1.pop(0)
            if not self.q1:
                break
            self.q2.append(x)
        while self.q2:
            y = self.q2.pop(0)
            self.q1.append(y)
        return x


    def top(self) -> int:
        while self.q1:
            x = self.q1.pop(0)
            self.q2.append(x)
        while self.q2:
            y = self.q2.pop(0)
            self.q1.append(y)
        return x

    def empty(self) -> bool:
        if len(self.q1) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
