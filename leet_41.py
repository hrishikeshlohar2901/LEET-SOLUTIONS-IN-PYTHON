# First missing positive

#https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] > 0 and nums[0]!=1:
                return 1
            elif nums[0]<=0:
                return 1
            else:
                return nums[0]+1
        else:
            a = [i for i in nums if i > 0]
            found=False
            a = set(a)
            a = list(a)
            a.sort()
            for count, j in enumerate(a, 1):
                if j != count:
                    found = True
                    return count
                    break
            if found == False and len(a)==0:
                return 1
            else:
                return a[-1] + 1
