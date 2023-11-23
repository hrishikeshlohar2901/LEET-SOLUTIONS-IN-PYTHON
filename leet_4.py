# median of two soted arrays 
# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n3 = nums1 + nums2
        n3.sort()
        n = len(n3)
        if n%2==0:
            sum = (n3[int((n/2)-1)] + n3[int(((n/2)+1)-1)]) / 2 # even median used by formula: (n/2th terms + n/2+1 th term )/2
            return sum
        else:
            sum = n3[int(((n/2)+0.5)-1)]  # for odd length (n/2 + 0.5)th term 
            return sum

                
        
