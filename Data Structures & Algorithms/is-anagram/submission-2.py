class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        my_dict = {}
        for i in range(len(s)):
            my_dict[s[i]] = 1 + my_dict.get(s[i],0)
            my_dict[t[i]] = my_dict.get(t[i],0) - 1 
        for j in my_dict.values():
            if j > 0:
                return False
        return True