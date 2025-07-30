# so lets assume we are given n, the number of nodes, and the parent list, where parent[i] is the parent of th node
# i think for this one, we are assuming we have a 
# also for the parents, array, rhe parent of the root will be -1 
import math
class KthAncestor:
    def __init__(self, n: int, parents: list[int]):
        self.parentgraph = [[] for _ in range(n)]
        for index, parent in enumerate(parents): 
            self.parentgraph[index].append(parent)
        self.bparents = [[] for _ in range(n)]
        self.b = math.floor(n ** .5)
        for index in range(n):
            self.bparents[index] = self.dfs(index)        
    def dfs(self, node: int):
        count = 0
        result = []
        nextnode = node
        result.append(nextnode)
        while count != self.b and nextnode != 0:
            nextnode = self.parentgraph[nextnode][0]
            count += 1
            result.append(nextnode)
        while count != self.b:
            result.append(-1)
            count +=1
        return result 


    def getkthancestor(self, node: int, k: int):
        while k != 0:
            if node == -1:
                return -1
            if k <= self.b:
                return self.bparents[node][k]
            node = self.bparents[node][self.b]    
            k -= self.b
            



