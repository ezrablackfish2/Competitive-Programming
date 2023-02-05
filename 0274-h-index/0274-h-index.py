class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        n, i = len(citations), 1
        while i <= n:
            print(n-i,citations[n-i],i)
            if citations[n-i] < i: break
            i += 1
        return i-1
        """
        :type citations: List[int]
        :rtype: int
        """
        