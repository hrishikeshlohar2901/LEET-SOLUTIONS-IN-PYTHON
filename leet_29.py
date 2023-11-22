# Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        elif dividend * divisor < 0 :
            if dividend < 0:
                dividend *= -1
            else:
                divisor *= -1
            return -1*(dividend // divisor)
        else:
            return dividend // divisor 

        
