class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        max_length = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            charset.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

sol = Solution()
print(sol.lengthOfLongestSubstring("abcabb"))