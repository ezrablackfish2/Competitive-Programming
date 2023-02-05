class Solution(object):
    def minNonZeroProduct(self, p):
        maxm = (2**p)-1
        mid = maxm // 2
        mod = (10**9)+7
        return (pow(maxm-1, mid, mod) * maxm) % mod
        """
        :type p: int
        :rtype: int
        """
        