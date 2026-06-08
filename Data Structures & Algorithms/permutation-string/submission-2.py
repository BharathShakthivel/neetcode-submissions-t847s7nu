class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        s2_dict = {}
        for i in range(len(s1)):
            s1_dict[s1[i]] = 1 + s1_dict.get(s1[i],0)
        l = 0
        for r in range(len(s2)):
            s2_dict[s2[r]] = 1 + s2_dict.get(s2[r],0)
            length = r - l + 1
            if length > len(s1):
                if s2_dict[s2[l]] == 1:
                    s2_dict.pop(s2[l])
                else:
                    s2_dict[s2[l]] -= 1
                l+=1
            if s1_dict == s2_dict:
                return True
        return False