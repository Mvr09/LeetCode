from functools import cache
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        @cache
        def backtrack(s, open, close):
            if len(s) == 2 * n:
                result.append(s)
                return
            if open < n:
                backtrack(s + "(", open + 1, close)
            if close < open:
                backtrack(s + ")", open, close + 1)

        result = []
        backtrack("", 0, 0)
        return result



