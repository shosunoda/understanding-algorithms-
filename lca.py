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
        curr = node
        while k:
            lowbit = k & -k
            exp = lowbit.bit_length() 

            curr   = self.binarystorage[curr][exp]
            if curr == -1:
                return -1
            k ^= lowbit
        return curr



class lca:
        def __init__(self,  parents: list[int]):
            n = len(parents)
            self.kthancestor = KthAncestor(n,parents)
            self.descendantgraph = [[] for _ in range(n)]
            for index, parent in enumerate(parents):
                if parent != -1:
                    self.descendantgraph[parent].append(index)
            self.powersoftwo = math.floor(math.log(n,2)) + 1
            

            self.depthchart = [0] * n
            self.dfs(0,0)

            return
            

        def dfs(self,node,level):
            self.depthchart[node] = level
            for child in self.descendantgraph[node]:
                self.dfs(child, level + 1)
            return 
        def lca(self, a, b):
            if self.depthchart[a] < self.depthchart[b]:
                a,b = b,a
            difference = self.depthchart[a] - self.depthchart[b]
            a = self.kthancestor.getkthancestor(a, difference)
            if a == b:
                return b
            for i in reversed(range(self.powersoftwo)):
                anc_a = self.kthancestor.getKthAncestor(a, 1<< i)
                anc_b = self.kthancestor.getKthAncestor(b, 1<< i)
                if anc_a != -1 and anc_a != anc_b:
                    a = anc_a
                    b = anc_b
            return self.kthancestor.getKthAncestor(a, 1)





