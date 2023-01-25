class Solution(object):
    def fizzBuzz(self, n):
        a = 1
        lister = []
        while a <= n:
            if a % 3 == 0:
                b = "Fizz"
                if a % 5==0:
                    b = "FizzBuzz"
                    lister.append(b)
                else:
                    lister.append(b)
            elif a % 5 == 0:
                b = "Buzz"
                lister.append(b)
            else:
                b = str(a)
                lister.append(b)
            a += 1
        print(lister)
        return lister
        """
        :type n: int
        :rtype: List[str]
        """