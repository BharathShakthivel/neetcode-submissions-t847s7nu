class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s)-ord('a')]+=1
            key = tuple(count)
            res[key].append(string)
        return list(res.values())