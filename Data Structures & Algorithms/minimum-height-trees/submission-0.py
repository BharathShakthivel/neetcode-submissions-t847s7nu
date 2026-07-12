class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj = defaultdict(list)
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        edj_count = {}
        leaves = deque()

        for node,neighbours in adj.items():
            edj_count[node] = len(neighbours)
            if edj_count[node]==1:
                leaves.append(node)
        
        while leaves:
            if n<=2:
                return list(leaves)

            for _ in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for neigh in adj[node]:
                    edj_count[neigh]-=1
                    if edj_count[neigh] == 1:
                        leaves.append(neigh)