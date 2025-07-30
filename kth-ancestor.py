import math
# for this one, we store powers of two 
class KthAncestor:
    def __init__(self, n: int, parents: list[int]):
        self.parentgraph = [[] for _ in range(n)]
        for index, parent in enumerate(parents): 
            self.parentgraph[index].append(parent)
        self.powersoftwo = math.floor(math.log(n,2)) + 1
        self.binarystorage = [[-1]*self.powersoftwo for _ in range(n)]
        for index in range(n):
            self.binarystorage[index][0] = self.parentgraph[index][0]
        for poweroftwo in range(1,self.powersoftwo):
            for nodes in range(1,n):
                previous = self.binarystorage[nodes][poweroftwo -1]
                if previous == -1:
                    self.binarystorage[nodes][poweroftwo] = -1
                else:
                    self.binarystorage[nodes][poweroftwo] = self.binarystorage[previous][poweroftwo - 1] 

    def getkthancestor(self, node: int, k: int):
        nextnode = node
        for exponent in range(self.powersoftwo):
            if k & (1 << exponent):
                nextnode = self.binarystorage[nextnode][exponent]
                if nextnode == -1:
                    return -1
        return nextnode
