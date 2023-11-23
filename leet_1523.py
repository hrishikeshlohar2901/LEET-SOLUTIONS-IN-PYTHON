#  Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a=(high-low)+1
        if a%2==0:
            return int(a/2)
        elif a%2!=0:
            if low%2!=0:
                return int(a/2 + 0.5)
            else:
                return int(a//2)
        
