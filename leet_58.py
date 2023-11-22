# Length of the last word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        d = s.split()
        a= d[len(d)-1]
        return len(a)
        
