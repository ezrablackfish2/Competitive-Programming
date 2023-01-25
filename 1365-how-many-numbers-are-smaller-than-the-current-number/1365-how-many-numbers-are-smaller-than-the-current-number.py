class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        c = 0
        lister = []
        for i in range(len(nums)):
            c = 0
            for k in range(len(nums)):
                if nums[i] > nums[k]:
                    c += 1
            lister.append(c)
        return lister
        """
        :type nums: List[int]
        :rtype: List[int]
        """