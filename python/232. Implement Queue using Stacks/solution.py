from collections import deque


class MyQueue:

  def __init__(self):
    self.queue = []
    # this also works
    # self.queue = deque()

  def push(self, x: int) -> None:
    self.queue.insert(0, x)
    # if using deque  
    # self.queue.appendleft(x)

  def pop(self) -> int:
    return self.queue.pop()

  def peek(self) -> int:
    return self.queue[-1]

  def empty(self) -> bool:
    return len(self.queue) == 0