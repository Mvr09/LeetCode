

class Solution:
    def bintodec(self,n):
        return int(n,2)
    def addBinary(self, a: str, b: str) -> str:
        return bin(self.bintodec(a) + self.bintodec(b))[2::1]






Sol = Solution()
