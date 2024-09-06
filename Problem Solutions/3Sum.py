from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seenSet = set()
        inventory = dict()

        for i in nums:
            if i not in seenSet:
                seenSet.add(i)
                inventory[i] = 1
            else:
                inventory[i] += 1

        result = []
        nums = list(seenSet)
        nums.sort()

        for i in range(len(nums)):
            a = nums[i]
            for j in range(i, len(nums)):
                b = nums[j]
                c = -(a + b)

                if c in inventory:
                    if (c == a and inventory[a] > 1) or (c == b and inventory[b] > 1) or (c != a and c != b):
                        triplet = sorted([a, b, c])
                        if triplet not in result:
                            result.append(triplet)

        return result
