class Solution(object):
    def numRescueBoats(self, people, limit):        
        people.sort(reverse=True)
        first = 0
        last = len(people)-1
        count = 0
        while first <= last:
            if people[first] + people[last] <= limit:
                first += 1
                last -= 1
            else:
                first += 1
            count += 1
        return count

        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        