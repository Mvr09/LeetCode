class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        if xstr!=xstr[::-1]:
            return False
        return True

Sol = Solution()
print(Sol.isPalindrome(122))