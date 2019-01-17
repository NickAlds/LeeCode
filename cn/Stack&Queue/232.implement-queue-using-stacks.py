"""
使用栈实现队列的下列操作：
push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。
你只能使用标准的栈操作 -- 也就是只有 push to top, peek/pop from top, size, 和 is empty 操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）。
"""

class MyQueue:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        stk = []
        while self.stack:
            stk.append(self.stack.pop())
        rst = stk.pop()
        while stk:
            self.stack.append(stk.pop())
        return rst
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        stk= []
        while self.stack:
            stk.append(self.stack.pop())
        rst = stk[-1]
        while stk:
            self.stack.append(stk.pop())
        return rst

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not len(self.stack)