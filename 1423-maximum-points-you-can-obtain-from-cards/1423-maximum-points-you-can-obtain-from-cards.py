class Solution(object):
    def maxScore(self, cardPoints, k):        
        left = 0
        right = len(cardPoints) - k
        total = sum(cardPoints[right:])
        
        ans = total
        for _ in range(k):
            total += cardPoints[left] - cardPoints[right]
            ans = max(ans, total)
            left += 1
            right += 1
        return ans
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        