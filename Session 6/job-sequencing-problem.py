class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = sorted(zip(deadline, profit), key=lambda x: x[1], reverse=True)
        max_deadline = max(deadline) if deadline else 0
        parent = list(range(max_deadline + 1))
        
        def find(i):
            node = i
            while parent[node] != node:
                # Path halving for faster future lookups
                parent[node] = parent[parent[node]] 
                node = parent[node]
            return node
        
        count_jobs = 0
        max_profit = 0
        
        for d, p in jobs:
            available_slot = find(d)
            
            if available_slot > 0:
                count_jobs += 1
                max_profit += p
                parent[available_slot] = find(available_slot - 1)
                
        return [count_jobs, max_profit]