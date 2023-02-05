class Solution(object):
    def shortestSubarray(self, nums, k):
        prefix = [0]
        monq = deque()
        minm = float('inf')
        for n in nums:
            prefix.append(n+prefix[-1])
        for idx, cur in enumerate(prefix):
            while monq and prefix[monq[-1]] >= cur:
                monq.pop()
            while monq and cur-prefix[monq[0]]>=k:
                minm = min(minm, idx-monq.popleft())
            monq.append(idx)
        return -1 if minm == float('inf') else minm

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        