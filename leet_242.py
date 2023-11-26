#valid Anagram
#https://leetcode.com/problems/valid-anagram/description/?envType=list&envId=prnw5ong

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a=''
        if len(t)!= len(s):
            return False
        else:
            b = list(s)
            for i in t:
                if i in b:
                    b.remove(i)
            if len(b)==0:
                return True
            else:
                return False
            
