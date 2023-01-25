class Solution(object):
    def kClosest(self, points, k):
        arr = []
        order = []
        lister = []
        l = 0
        for x, y in points:
            i = x**2 + y**2
            arr.append([i, x, y])
        print(arr)
        heapq.heapify(arr)
        while k > 0:
            small = heapq.heappop(arr)
            lister.append(small)
            k -= 1
        for i, x, y in lister:
            order.append([x, y])
        print(order)
        return order
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """