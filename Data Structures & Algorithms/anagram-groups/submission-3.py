class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        ans = defaultdict(list)
        
        for string in strs:
            key = [0] * 26
            for s in string:
                key[ord(s) - ord('a')]+=1
            ans[tuple(key)].append(string)
        return list(ans.values())