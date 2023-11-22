# longest substring without repeating characters 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        flag = False
        sample = False
        a=''
        if len(s)==1:
            flag = True
            a = s
        else:
            for i in range(0,len(s)):
                name = ''
                for j in range(i,len(s)):
                    if s[j] not in name:
                        name = name + s[j]
                        if j == (len(s)-1):
                            sample = True
                            if len(name)>len(a):
                                flag = True
                                a=''
                                a=name
                                break
                    elif len(name) > len(a):
                        flag = True
                        a=''
                        a = name
                        break
                    else:
                        break
        if flag == False:
            return len(s)
        else:                
            return len(a)
