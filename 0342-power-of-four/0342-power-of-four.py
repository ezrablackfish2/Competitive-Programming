class Solution(object):
    def isPowerOfFour(self, n):
        return n != 0 and n & (n-1) == 0 and n & 1431655765 == n
        """
        :type n: int
        :rtype: bool
        """
        