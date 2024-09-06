def romanToInt(self, s: str) -> int:
    vals = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and vals[str(s[i])] < vals[str(s[i + 1])]:
            ans -= vals[str(s[i])]
        else:
            ans += vals[str(s[i])]
    return ans