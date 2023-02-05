class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        hash = {}
        monStack = [nums2[0]]
        for n in nums2:
            while monStack and n > monStack[-1]:
                hash[monStack.pop()] = n
            monStack.append(n)
        for n in monStack:
            hash[n] = -1
        res = []
        for n in nums1:
            res.append(hash[n])
        return res


        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        