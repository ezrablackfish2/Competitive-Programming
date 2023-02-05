class Solution(object):
    def findTheWinner(self, n, k):
        arr=[i for i in range(1,n+1)]
        def rec(index,k):
            if len(arr) == 1:
                return
            index=(index + k)%len(arr)
            arr.pop(index)
            rec(index,k)
        rec(0,k-1)
        return arr[0]

        """
        :type n: int
        :type k: int
        :rtype: int
        """
        