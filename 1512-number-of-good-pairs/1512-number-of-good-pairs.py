class Solution(object):
    def numIdenticalPairs(self, nums):
        good = 0
        for i in range(len(nums)):

            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    good += 1
        print(good)
        return good
        """
        :type nums: List[int]
        :rtype: int
        """