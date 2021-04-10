import pickle as pickle
import math
class Karatsuba:
    def memoize(func):
        cache = {}
        def wrapper(*args, **kwargs):
            key = pickle.dumps(args) + pickle.dumps(kwargs)
            if key not in cache:
                cache[key] = func(*args, **kwargs)
            return cache[key]
        return wrapper

    def __init__(self, inputA, inputB):
        self.recursiveCalls = 0
        self.inputA = inputA
        self.inputB = inputB
        self.inputA, self.inputB = str(self.inputA), str(self.inputB)
        while len(self.inputA) < len(self.inputB) or not self.isPowerOfTwo(len(self.inputA)):
            self.inputA = "0" + self.inputA
        while len(self.inputB) < len(self.inputA) or not self.isPowerOfTwo(len(self.inputB)):
            self.inputB = "0" + self.inputB
        if not self.isPowerOfTwo(len(self.inputA)):
            raise Exception("Digits not a power of 2", self.inputA) 
        if not self.isPowerOfTwo(len(self.inputB)):
            raise Exception("Digits not a power of 2", self.inputB)
        if len(self.inputA) != len(self.inputB):
            raise Exception("input size must match", self.inputA, self.inputB)

    def Log2(self,x):
        if x == 0:
            return False
        return (math.log10(x) /
                math.log10(2))
    
    # Function to check
    # if x is power of 2
    def isPowerOfTwo(self,n):
        return (math.ceil(self.Log2(n)) ==
                math.floor(self.Log2(n)))
    #Splitting string into equal halves
    def splitString(self,s):
        return s[:len(s)//2], s[len(s)//2:]

    def solve(self):
        return self.solveRecursive(self.inputA, self.inputB)
        
    @memoize
    def solveRecursive(self, inputA, inputB):
        self.recursiveCalls += 1
        n = len(inputA)
        if n <= 1:
            return int(inputA)*int(inputB)
        a, b = self.splitString(inputA)
        c, d = self.splitString(inputB)
        p, q = str(int(a)+int(b)), str(int(c)+int(d))
        ac = self.solveRecursive(a,c)
        bd = self.solveRecursive(b,d)
        while len(p) < len(q) or not self.isPowerOfTwo(len(p)):
            p = "0" + p
        while len(q) < len(p) or not self.isPowerOfTwo(len(q)):
            q = "0" + q
        pq = self.solveRecursive(p,q)
        adbc = pq - ac - bd
        return 10**n * ac + 10**(n//2) * adbc + bd
    
    def printRecursiveCalls(self):
        print('Karatsuba', self.recursiveCalls)
    memoize = staticmethod( memoize )
