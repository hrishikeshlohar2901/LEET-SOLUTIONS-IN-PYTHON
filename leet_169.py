# Majority Element
# https://leetcode.com/problems/majority-element/submissions/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        nums.sort()
        i=0
        while i<len(nums):
            if nums.count(nums[i])>n:
                return nums[i] 
                i=i+nums.count(nums[i])
            else:
                i=i+nums.count(nums[i])
