class Solution(object):
    def totalFruit(self, fruits):        
        basket = {}
        left = 0
        
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1

            if len(basket) > 2:
                basket[fruits[left]] -= 1
                
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        
        return right - left + 1
        """
        :type fruits: List[int]
        :rtype: int
        """
        