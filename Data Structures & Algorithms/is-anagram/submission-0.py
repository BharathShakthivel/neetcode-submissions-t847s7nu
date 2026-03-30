class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        for string in s:
            dict_s[string] = 1 + dict_s.get(string,0) 
        for string in t:
            dict_t[string] = 1 + dict_t.get(string,0)
        if dict_s == dict_t:
            return True
        return False        
        