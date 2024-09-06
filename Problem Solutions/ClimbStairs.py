from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

sol = Solution()
print(sol.climbStairs(5))  # Output: 8
