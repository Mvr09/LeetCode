class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        numstr = "".join(map(str,digits))
        num = int(numstr)
        num+=1
        return [int(digit) for digit in str(num)]