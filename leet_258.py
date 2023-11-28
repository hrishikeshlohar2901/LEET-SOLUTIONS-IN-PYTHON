# add digits

#https://leetcode.com/problems/add-digits/submissions/

class Solution:
    def addDigits(self, num: int) -> int:
        while num>9:
            s=0
            while num: # a numerical value of 0 is often considered equivalent to "false," and any non-zero value is considered equivalent to "true." 
                s+=num%10
                num=num//10
            num = s
        return num
        
