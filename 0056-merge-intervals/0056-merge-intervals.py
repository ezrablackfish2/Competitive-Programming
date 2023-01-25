class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        print(intervals)
        lister = [intervals[0]]
        for x, y in intervals[1:]:
            if x > lister[-1][1]:
                lister.append([x, y])
            elif y > lister[-1][1]:
                lister[-1][1] = y
                print(lister)
        return lister

        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """