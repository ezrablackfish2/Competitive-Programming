class Solution(object):
    def rotate(self, nums, k):
        first = 0
        second = k
        tempList = nums[:]
        for i in range(len(nums)):
            second = second % len(nums)
            nums[second] = tempList[first]
            first += 1
            second +=1
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        