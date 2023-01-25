class Solution(object):
    def largestNumber(self, nums):
        for i, n in enumerate(nums):
            nums[i] = str(n)

        def compare(second, first):
            if second + first > first + second:
                return -1
            else:
                return 1

        finale = sorted(nums, key=functools.cmp_to_key(compare))
        stringer = ""
        print('"{}"'.format(stringer.join(finale)))
        return str(int(stringer.join(finale)))
        """
        :type nums: List[int]
        :rtype: str
        """