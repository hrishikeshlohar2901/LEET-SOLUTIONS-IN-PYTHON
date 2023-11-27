# Plus One
# https://leetcode.com/problems/plus-one/description/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        a=[]
        for i in digits:
            s=s+str(i)
        s = int(s)+1
        for j in str(s):
            a.append(int(j))
        return a
        
