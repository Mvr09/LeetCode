from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            char = s[i]
            if char in "{[(":
                stack.append(char)
            elif char in "]})":
                if stack:
                    if char == stack.pop():
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


sol = Solution()
print(sol.isValid("(]"))
