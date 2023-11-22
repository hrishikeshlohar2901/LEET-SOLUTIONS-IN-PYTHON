# Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = a[::-1]
        b1 = b[::-1]
        s = 0
        d=0
        w=''
        if a == '0' and b=='0':
            return '0'
        else:
            for i in range(0,len(a)):
                n = int(a1[i])
                s = s+(n*(2**i))           
            for j in range(0,len(b)):
                n = int(b1[j])
                d = d+(n*(2**j))
            sum = s+d
            while sum!=0:
                n = sum % 2
                w = w+str(n)
                sum = sum//2

        return w[::-1]
        
