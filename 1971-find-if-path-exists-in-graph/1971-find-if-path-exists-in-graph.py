class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hmap = collections.defaultdict(list)
        for i, j in edges:
            hmap[i].append(j)
            hmap[j].append(i)
        seen = set()
        def dfs(node): 
            if node == destination:
                return True 
            seen.add(node)
            for i in hmap[node]:
                if i not in seen and dfs(i): 
                    return True 
            return False
        return dfs(source )
        