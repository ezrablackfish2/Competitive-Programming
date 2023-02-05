class Solution(object):
    def reverseParentheses(self, s):
        res = ['']
        for c in s:
            if c == '(':
                res.append('')
            elif c == ')':
                res[len(res) - 2] += res.pop()[::-1]
            else:
                res[-1] += c
            print(res)
        return "".join(res)
    
        """
        :type s: str
        :rtype: str
        """
        