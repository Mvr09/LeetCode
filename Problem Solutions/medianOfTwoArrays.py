import statistics
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        return statistics.median(nums)


Sol = Solution()
print(Sol.findMedianSortedArrays([1, 3], [2]))
