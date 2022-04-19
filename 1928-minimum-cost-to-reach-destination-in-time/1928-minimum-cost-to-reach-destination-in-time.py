class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        graph = defaultdict(lambda: defaultdict(lambda: math.inf))
        n = len(passingFees)
        for s,e,t in edges:
            graph[s][e] = min(graph[s][e], t)
            graph[e][s] = min(graph[e][s], t)
        times = [math.inf] * n
        costs = [math.inf] * n
        times[0] = 0
        costs[0] = passingFees[0]
        
        heap = [(passingFees[0], 0, 0)]
        
        while heap:
            currentCost, currentTime, node = heappop(heap)
            if node == n-1 and currentTime <= maxTime:
                return currentCost
            if currentTime > maxTime or (currentCost > costs[node] and currentTime > times[node]): 
                continue
            for nei in graph[node]:
                if currentTime + graph[node][nei] < times[nei] or currentCost + passingFees[nei] < costs[nei]:
                    times[nei] = min(times[nei], currentTime + graph[node][nei])
                    costs[nei] = min(costs[nei], currentCost + passingFees[nei])
                    heappush(heap,(currentCost + passingFees[nei], currentTime + graph[node][nei], nei))
        
        return -1
    
    