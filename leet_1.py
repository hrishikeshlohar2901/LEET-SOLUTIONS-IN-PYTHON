#two sum
#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        flag = False
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    flag = True
                    #print('Result = {} and {}'.format(nums[i],nums[j]))  
                    return [i,j]           
        if flag == False:
            print('The number does not exist')

        
