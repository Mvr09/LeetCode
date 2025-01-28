import statistics
import math

class MedianFinder:

    def __init__(self):
        self.lst = []
    def addNum(self, num: int) -> None:
        self.lst.append(num)
    def findMedian(self) -> float:
        return statistics.median(self.lst)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()