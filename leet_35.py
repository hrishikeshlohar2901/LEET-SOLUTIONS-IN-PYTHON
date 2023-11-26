#Search inserted position
#https://leetcode.com/problems/search-insert-position/description/?envType=list&envId=prnw5ong

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (low + high)//2
            if target<nums[mid]:
                high = mid-1
            elif target>nums[mid]:
                low = mid+1
            else:
                return mid
        return low


            
        
        
