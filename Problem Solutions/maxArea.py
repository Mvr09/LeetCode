from functools import cache
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        @cache
        def areaCalc(a,b,l,r):
            return min(a,b)*(r-l)

        while left < right:
            area = areaCalc(height[left], height[right],left,right)
            if area > maxWater:
                maxWater = area

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
