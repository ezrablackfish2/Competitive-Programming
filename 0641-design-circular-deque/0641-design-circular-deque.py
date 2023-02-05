class MyCircularDeque(object):

    def __init__(self, k):
        self.k = k
        self.deque = []        
        self.i = 0
        """
        :type k: int
        """
        

    def insertFront(self, value):
        if self.i < self.k:
            self.deque.insert(0,value)
            self.i+=1
            return True
        return False
        """
        :type value: int
        :rtype: bool
        """
        

    def insertLast(self, value):
        if self.i < self.k:
            self.deque.append(value)
            self.i+=1   
            return True
        return False 
        """
        :type value: int
        :rtype: bool
        """
        

    def deleteFront(self):
        if self.i > 0:
            self.deque.pop(0)
            self.i-=1
            return True
        return False  
        """
        :rtype: bool
        """
        

    def deleteLast(self):
        if self.i > 0:
            self.deque.pop()
            self.i-=1
            return True
        return False
        """
        :rtype: bool
        """
        

    def getFront(self):
        if len(self.deque) == 0:
            return -1 
        return self.deque[0]   
        """
        :rtype: int
        """
        

    def getRear(self):
        if len(self.deque) == 0:
            return -1 
        return self.deque[-1]
        """
        :rtype: int
        """
        

    def isEmpty(self):
        if len(self.deque) == 0:
            return True
        return False
        """
        :rtype: bool
        """
        

    def isFull(self):
        if len(self.deque) == self.k:
            return True
        return False
    
        """
        :rtype: bool
        """
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()