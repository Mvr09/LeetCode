from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        guide = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        def backtrack(index: int, path: str):
            if index == len(digits):
                combinations.append(path)
                return
            for letter in guide[digits[index]]:
                backtrack(index + 1, path + letter)

        combinations = []
        backtrack(0, "")
        return combinations


sol = Solution()
print(sol.letterCombinations("23"))
