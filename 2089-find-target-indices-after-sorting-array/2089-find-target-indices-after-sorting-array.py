class Solution(object):
    def targetIndices(self, nums, target):
        lister = []
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                small = i
                if nums[k] < nums[i]:
                    temp = nums[i]
                    nums[i] = nums[k]
                    nums[k] = temp
        for j in range(len(nums)):
            if nums[j] == target:
                lister.append(j)
        print(lister)
        print(nums)
        return lister
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """