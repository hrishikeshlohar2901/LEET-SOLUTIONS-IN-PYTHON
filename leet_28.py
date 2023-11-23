# Find the Index of the First Occurence in String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        b = 0
        if needle in haystack:
            for i in range(len(haystack)):
                if haystack[i] == needle[0]:
                    for j in range(i, len(haystack)):
                        name = haystack[i:j+1]  # Simplify the substring extraction
                        if name == needle:
                            b = i
                            return b
            return b
        else:
            return -1

