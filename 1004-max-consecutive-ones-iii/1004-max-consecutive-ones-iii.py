class Solution(object):
    def longestOnes(self, nums, k):        
        beg, end, zeros, ans = 0, 0, 0, 0
        while end < len(nums):
            if zeros + (nums[end]==0) <= k:
                zeros += (nums[end]==0)
                ans = max(ans, end-beg+1)
                end += 1
            else:
                zeros -= (nums[beg]==0)
                beg += 1
        return ans
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        