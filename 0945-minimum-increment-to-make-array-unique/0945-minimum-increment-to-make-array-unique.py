class Solution(object):
    def minIncrementForUnique(self, nums):
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(1,n):
            if nums[i] <= nums[i-1]:
                # this is the case for making item unique
                diff = nums[i-1] + 1 - nums[i]
                ans += diff
                nums[i] = nums[i-1] + 1
        return ans
        """
        :type nums: List[int]
        :rtype: int
        """
        