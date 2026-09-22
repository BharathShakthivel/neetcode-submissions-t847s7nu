class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest_sub_string = 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l+=1
            window.add(s[r])
            longest_sub_string = max(longest_sub_string,(r-l) +1)
        return longest_sub_string