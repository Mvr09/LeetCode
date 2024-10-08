
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif (n & 1) != 0:
            return x * self.myPow(x * x, n // 2)
        else:
            return self.myPow(x * x, n // 2)
