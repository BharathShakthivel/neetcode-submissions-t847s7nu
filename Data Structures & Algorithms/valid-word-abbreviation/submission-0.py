class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i, j = 0, 0
        while (i < len(word)) and (j < len(abbr)):
            if abbr[j] == '0':
                return False
            if word[i] == abbr[j]:
                i+=1
                j+=1
            elif abbr[j].isalpha():
                return False
            else:
                sublen = 0
                while j < len(abbr) and abbr[j].isdigit():
                    sublen = sublen * 10 + int(abbr[j])
                    j+=1
                i+=sublen
        if i == len(word) and j == len(abbr):
            return True
        return False