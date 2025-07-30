# Given an array arr, after O(n log n) preprocessing, you can answer queries of the form:

# What is the maximum (or minimum) in the range arr[L..R]?

# in O(1) time.

import math

class SparseTable:
    def __init__(self, arr, func):
      
        self.arr = arr
        self.func = func
        self.n = len(arr)
        self.LOG = math.floor(math.log2(self.n)) + 1
        self.st = [[0] * self.LOG for _ in range(self.n)]
        self.build()

    def build(self):
        for i in range(self.n):
            self.st[i][0] = self.arr[i]

        for j in range(1, self.LOG):
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = self.func(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])

    def query(self, l, r):

        length = r - l + 1
        k = length.bit_length() - 1
        return self.func(self.st[l][k], self.st[r - (1 << k) + 1][k])