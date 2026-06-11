class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        pre_map = defaultdict(list)
        #  We use hashmap to stroe the pre requisites for corresponding courses.
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
        # We need to keep track of the visited courses to detect cycles and return False
        visit = set()

        #  Defining DFS:
        def dfs(crs):
            if crs in visit:
                return False
                # Means the course has already been a prereq.
            if pre_map[crs] == []:
                return True
                #  Means there are not prereq to be visited for current course
            visit.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre): return False
            pre_map[crs] == []
            visit.remove(crs)
            return True
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
            