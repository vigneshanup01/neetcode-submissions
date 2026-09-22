import statistics
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l3=nums1+nums2

        median=statistics.median(l3)


        return median
        
        