class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        n = len(nums)
        x = len(l)
        arr = [True] * x
        for i in range(x):
            u = nums[l[i] : r[i] + 1]
            u.sort()
            for j in range(len(u) - 2):
                if u[j + 1] - u[j] != u[j + 2] - u[j + 1]:
                    arr[i] = False
                    break 
        return arr
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """