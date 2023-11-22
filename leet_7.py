# Reverse Integer

class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            x = -1*x
            x = str(x)
            rev = x[::-1]
            rev = -1*int(rev)
            if rev < -2147483648:
                return 0
            else:
                return rev
        else:
            x = str(x)
            rev = x[::-1]
            rev = int(rev)
            if rev > 2147483647:
                return 0
            else:
                return rev
        
