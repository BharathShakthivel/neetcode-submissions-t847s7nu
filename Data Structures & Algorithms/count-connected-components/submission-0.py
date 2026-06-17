class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        pre_map = defaultdict(list)
        for u,v in edges:
            pre_map[u].append(v)
            pre_map[v].append(u)
        visited=set()
        components = 0
        def dfs(node):
                visited.add(node)
                for neigh in pre_map[node]:
                    if neigh not in visited:
                        dfs(neigh)
                
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                components+=1
        return components