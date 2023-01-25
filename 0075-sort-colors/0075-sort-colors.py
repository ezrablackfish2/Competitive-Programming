class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        print(nums)
        return nums
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """