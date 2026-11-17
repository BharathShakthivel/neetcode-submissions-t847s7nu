class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution with more space
        # if len(s)!= len(t):
        #     return False
        # my_dict_s = {}
        # my_dict_t = {}

        # for i in range(len(s)):
        #     my_dict_s[s[i]] = 1 + my_dict_s.get(s[i],0)
        # for j in range(len(s)):
        #     my_dict_t[t[j]] = 1 + my_dict_t.get(t[j],0)
        
        # if my_dict_s == my_dict_t:
        #     return True
        # else:
        #     return False

        # Solution with less space
        # if len(s)!= len(t):
        #     return False
        # my_dict = {}
        # for i in range(len(s)):
        #     my_dict[s[i]] = 1 + my_dict.get(s[i],0)
        #     my_dict[t[i]] = my_dict.get(t[i],0) - 1 
        # for j in my_dict.values():
        #     if j > 0:
        #         return False
        # return True


































        freq_dict = {}
        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            freq_dict[s[i]] = freq_dict.get(s[i],0)+1
        for j in range(len(t)):
            freq_dict[t[j]] = freq_dict.get(t[j],0)-1
        
        for k in freq_dict.values():
            if k > 0:
                return False
        return True
















