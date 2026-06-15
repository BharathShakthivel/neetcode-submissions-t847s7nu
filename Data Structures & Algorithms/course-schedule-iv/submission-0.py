class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        from collections import defaultdict
        pre_map = defaultdict(list)
        for pre,crs in prerequisites:
            pre_map[crs].append(pre)
        
        prereq_map = {}
        def dfs(crs):
            if crs not in prereq_map:
                prereq_map[crs] = set()
                for neigh in pre_map[crs]:
                    dfs(neigh)
                    prereq_map[crs] |= prereq_map[neigh]
                prereq_map[crs].add(crs)
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for u,v in queries:
            res.append(u in prereq_map[v])
        return res