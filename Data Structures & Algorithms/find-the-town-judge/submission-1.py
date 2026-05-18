class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if n ==1:
        #     return 1
        # from collections import defaultdict
        # incoming = defaultdict(int)
        # outgoing = defaultdict(int)
        # for src,dist in trust:
        #     incoming[dist]+=1
        #     outgoing[src]+=1
        # for i in range(1,n+1):
        #     if incoming[i] == (n-1) and outgoing[i] == 0:
        #         return i
        # return -1 

        # Delta method with reduced space Delta = incoming - outgoing = n-1 -0 => n-1
        if n ==1:
            return 1
        from collections import defaultdict
        delta = defaultdict(int)
        for src,dist in trust:
            delta[src]-=1
            delta[dist]+=1
        for i in range(1,n+1):
            if delta[i] == (n-1):
                return i
        return -1 