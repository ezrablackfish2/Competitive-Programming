class MyQueue(object):

    def __init__(self):
        self.queue = [] 
        

    def push(self, x):
        self.queue.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
        """
        :rtype: int
        """
        

    def peek(self):
        return self.queue[0]
        
        """
        :rtype: int
        """
        

    def empty(self):
        if len(self.queue)== 0:
            return True            
        else:
            return False
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()