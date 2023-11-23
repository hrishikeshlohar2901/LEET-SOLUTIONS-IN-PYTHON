# Valid Palindrome
#https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=''
        for i in s:
            if i.isalpha() or i.isnumeric():
                a = a + i
            else:
                continue
            
        if a.lower() == a[::-1].lower():
            return True
        else:
            return False

        
