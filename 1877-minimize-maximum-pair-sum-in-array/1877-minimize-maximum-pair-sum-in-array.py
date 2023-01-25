class Solution(object):
    def minPairSum(self, nums):
        nums = sorted(nums)
        i, j, res, sum = 0, len(nums) - 1, 0, 0
        while i < j:
            sum = nums[i] + nums[j]
            res = max(res, sum)
            i += 1
            j -= 1
        print(res)
        return res


        """
        :type nums: List[int]
        :rtype: int
        """