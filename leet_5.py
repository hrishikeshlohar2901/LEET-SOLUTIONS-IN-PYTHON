#Longest palindromic substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        name = ''
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j+1]

                if substring == substring[::-1] and len(substring) > len(name):
                    name = substring

        return name
