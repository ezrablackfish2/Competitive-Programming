class Solution(object):
    def kthLargestNumber(self, nums, k):
        array = list(map(lambda x: -int(x), nums))
        heapq.heapify(array)
        while k > 0:
            max = heapq.heappop(array)
            k -= 1

        print('"{}"'.format(-max))
        return "{}".format(-max)
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """