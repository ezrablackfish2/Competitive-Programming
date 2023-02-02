class Solution(object):
    def topKFrequent(self, nums, k):
        lister = []
        final = []
        frequency = collections.Counter(nums)
        for i, j in frequency.items():
            lister.append([i, j])
            m = 0
        for m in range(len(nums)):
            max = 0
            for l in range(m + 1, len(lister)):
                if lister[l][-1] > lister[m][-1]:
                    lister[l], lister[m] = lister[m], lister[l]
        i = 0
        while k > 0:
            final.append(lister[i][0])
            i += 1
            k -= 1
        print(max)
        print(lister)
        print(final)
        return final


        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        