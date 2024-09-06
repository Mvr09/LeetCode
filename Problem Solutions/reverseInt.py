class Solution:
    def reverse(self, x: int) -> int:
        xstrinverted = int(str(x)[::-1])

        if xstrinverted>=-2147483648 and xstrinverted<=2147483648:
            return int(xstrinverted)
        else:
            return 0