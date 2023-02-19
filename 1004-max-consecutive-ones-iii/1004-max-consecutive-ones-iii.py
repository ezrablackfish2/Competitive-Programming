class Solution(object):
    def longestOnes(self, nums, k):
        window_count = 0
        l = 0
        ans  = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                window_count += 1
            
            # once the zero counter becomes greater than k, 
            # we need to shrink the window and decrement it's count
            # so, We increment left only if we have exhausted our flips ,otherwise keep incrementing right
            while window_count > k:
                if nums[l] == 0:
                    window_count -= 1
                l += 1
                
            ans = max(ans, r - l + 1)

        return ans
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        