class Solution:
    def intToendStr(self, num: int) -> str:
        endStr = ""
        storeInt = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"],
                    [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"],
                    [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        for i in range(len(storeInt)):
            while num >= storeInt[i][0]:
                endStr += storeInt[i][1]
                num -= storeInt[i][0]
        return endStr