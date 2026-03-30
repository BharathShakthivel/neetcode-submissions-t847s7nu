class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_string = ""
        cur_num = 0

        for ch in s:
            if ch.isdigit() == True:
                cur_num = cur_num * 10 + int(ch)
            elif ch == "[":
                stack.append((cur_num,cur_string))
                cur_num = 0
                cur_string = ""
            elif ch == "]":
                repeat,prev_string = stack.pop()
                cur_string =  prev_string + (repeat * cur_string)
                res = cur_string
            else:
                cur_string+=ch
        return cur_string
