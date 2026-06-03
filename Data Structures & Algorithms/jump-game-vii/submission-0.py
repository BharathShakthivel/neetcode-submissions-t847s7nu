class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        farthest = 0
        from collections import deque
        q = deque([0])
        n = len(s)
        while q:
            i = q.popleft()
            start = max(i+minJump, farthest+1)
            stop = i + maxJump + 1
            for j in range(start, min(stop,n)):
                if s[j] == '0':
                    q.append(j)
                    if j == n-1:
                        return True
            farthest = stop -1
        return False