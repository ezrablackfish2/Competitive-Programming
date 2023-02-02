class Solution(object):
    def minSetSize(self, arr):

        c = collections.Counter(arr)
        freq = list(c.values())
        freq.sort()

        ans, removed, half = 0, 0, len(arr) // 2
        while removed < half:
            ans += 1
            removed += freq.pop()
        print(arr)
        print(ans)
        return ans
        """
        :type arr: List[int]
        :rtype: int
        """
        