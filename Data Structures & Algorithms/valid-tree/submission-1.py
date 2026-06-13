class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        from collections import defaultdict
        edge_map = defaultdict(list)
        for n1,n2 in edges: # Undirected so we must connect both the edges
            edge_map[n1].append(n2)
            edge_map[n2].append(n1)
        visit = set()
        def dfs(i,prev):
            if i in visit: # If we encounter already visited node, it becomes a cycle and hence it is not a tree
                return False
            visit.add(i)
            for neighbour in edge_map[i]:
                if neighbour == prev: # Basically skipping the neighbour if it is the prev value
                    continue
                if not dfs(neighbour,i): # IF the dfs returns False, we return False as well.
                    return False
            return True # We traversed all nodes and found it to be a tree structure
        return dfs(0,-1) and n == len(visit) # We must return True only if all the nodes and visited.