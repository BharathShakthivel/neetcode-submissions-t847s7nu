class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        valid = path.split("/")
        for i in valid:
            if i =="." or i =="":
                continue
            elif i == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+ "/".join(stack)
