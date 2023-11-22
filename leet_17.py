# Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        if len(digits)==1:
            a = dict[digits]
            my_list = []
            for i in a:
                my_list.append(i)
            return my_list
        elif len(digits)>1:
            if len(digits)==2:
                a = dict[digits[0]] #2 : abc
                b = dict[digits[1]] #3: def
                my_list=[]
                for i in a:
                    for j in b:
                        c = i+j
                        my_list.append(c)
                return my_list
            elif len(digits)==3:
                a = dict[digits[0]]
                b = dict[digits[1]]
                c = dict[digits[2]]
                my_list=[]
                for i in a:
                    for j in b:
                        for k in c:
                            d = i+j+k
                            my_list.append(d)
                return my_list
            elif len(digits)==4:
                a = dict[digits[0]]
                b = dict[digits[1]]
                c = dict[digits[2]]
                d = dict[digits[3]]
                my_list=[]
                for i in a:
                    for j in b:
                        for k in c:
                            for l in d:
                                e = i+j+k + l
                                my_list.append(e)
                return my_list

                
        
