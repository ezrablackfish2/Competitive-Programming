class Solution(object):
    def maxOperations(self, nums, k):
        nums = sorted(nums)
        i, j, l = 0, len(nums) - 1, 0
        while i < j:
            if nums[i] + nums[j] < k:
                i += 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                print(k)
                nums.pop(i)
                nums.insert(i, 0)
                nums.pop(j)
                nums.insert(j, 0)
                i += 1
                j -= 1
                l += 1
        print(nums)
        print(l)
        return l
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """