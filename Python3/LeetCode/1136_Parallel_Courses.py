class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        if N <= 1:return N
        
        indegree = [0 for _ in range(N)]
        adj_list = defaultdict(list)
        for x, y in relations:
            adj_list[x].append(y)
            indegree[y-1] += 1
            
        q = deque([])
        
        visited = set()
        for i, curr in enumerate(indegree):
            if curr == 0:
                q.append(i+1)
                
        if len(q) == 0:
            return -1
        
        res = 0
        while q:
            size = len(q)
            while size != 0:
                curr = q.popleft()
                visited.add(curr)
                for dependant in adj_list[curr]:
                    indegree[dependant - 1] -= 1
                    if indegree[dependant - 1] == 0 and dependant not in visited:
                        q.append(dependant)
                size -= 1
            res += 1
        
        if len(visited) < N:
            return -1
        
        return res
