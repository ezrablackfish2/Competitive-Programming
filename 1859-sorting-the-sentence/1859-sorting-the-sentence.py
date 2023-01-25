class Solution(object):
    def sortSentence(self, s):
        arr = s.split()
        final = ""
        for i in range(len(arr)):
            minimum_index = i
            for j in range(i + 1, len(arr)):
                if arr[j][-1] < arr[minimum_index][-1]:
                    minimum_index = j
            if minimum_index != i:
                temp = arr[minimum_index]
                arr[minimum_index] = arr[i]
                arr[i] = temp
            final += arr[i][:-1] + " "
        return final[:-1]
        """
        :type s: str
        :rtype: str
        """