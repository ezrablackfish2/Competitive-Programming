class Solution(object):
    def rearrangeArray(self, nums):
        def change(l, r):
            nums[l], nums[r] = nums[r], nums[l]
                    
        n = len(nums)
        for i in range(1, n-1):
            prev, cur, nxt = nums[i-1], nums[i], nums[i+1]

            if prev < cur < nxt or prev > cur > nxt:
                change(i+1, i)
                        
        return nums
        """
        :type nums: List[int]
        :rtype: List[int]
        """