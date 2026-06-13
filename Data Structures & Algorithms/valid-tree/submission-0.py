class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        from collections import defaultdict
        edge_map = defaultdict(list)
        for n1,n2 in edges:
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)
        visit = set()
        def dfs(i,prev):
            if i in visit:
                return False
            visit.add(i)
            for neighbour in edge_map[i]:
                if neighbour == prev:
                    continue
                if not dfs(neighbour,i):
                    return False
            return True
        return dfs(0,-1) and n == len(visit)