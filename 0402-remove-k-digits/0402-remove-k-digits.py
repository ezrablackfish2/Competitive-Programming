class Solution(object):
    def removeKdigits(self, num, k):
        stk = []
        for i in range(len(num)):
            while stk and int(num[i]) < int(stk[-1]) and k:
                stk.pop()
                k -= 1
            stk.append(num[i])
        res = ""
        begin = False
        for n in stk:
            if n != '0':
                begin = True
            if begin:
                res += n
        res = res[:-k] if k else res
        return "0" if res == "" else res


        """
        :type num: str
        :type k: int
        :rtype: str
        """
        