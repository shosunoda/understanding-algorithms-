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
        return
    def dfs(self, node: int):
        count = 0
        result = []
        nextnode = node
        while count != self.b and nextnode != -1:
            nextnode = self.parentgraph[nextnode][0]
            count += 1
            result.append(nextnode)
        while count != self.b:
            result.append(-1)
            count +=1
        return result 


    def getkthancestor(self, node: int, k: int):
        nextnode = node
        if k == 0:
            return nextnode
        while k >= self.b:
            nextnode = self.bparents[nextnode][self.b-1]
            k -= self.b
        return self.bparents[nextnode][k -1 ]
            



