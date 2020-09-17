import math
class Solution(object):
    def bulbSwitch(self, n):
        """
        type n: int
        rtype: int
        """
        return int(math.sqrt(n))
val=Solution()
n=int(input())
print(val.bulbSwitch(n))
