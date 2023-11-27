# group anagrams
# https://leetcode.com/problems/group-anagrams/description/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)
        for i in strs:
            a = ''.join(sorted(i))
            l[a].append(i)
        return list(l.values())
