class Solution(object):
    def findOriginalArray(self, changed):
        n = len(changed)
        print(n % 2)
        if n % 2 != 0:
            return []

        count = collections.Counter(changed)
        print(count)
        changed.sort()
        print(changed)
        ans = []
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                ans.append(num)
            elif num > 0 and count[num] and count[num * 2]:
                count[num] -= 1
                count[num * 2] -= 1
                ans.append(num)
        print(ans)
        return ans if len(ans) == n // 2 else []
        """
        :type changed: List[int]
        :rtype: List[int]
        """