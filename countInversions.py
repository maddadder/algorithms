import math

class CountInversions:

    def __init__(self, items):
        self.recursiveCalls = 0
        self.items = items

    #Splitting string into equal halves
    def splitArray(self,s):
        return s[:len(s)//2], s[len(s)//2:]

    def solve(self):
        return self.solveRecursive(self.items)

    def merge(self, a, b, n):
        inversionCount = 0
        result = [0] * n
        a = a + [math.inf]
        b = b + [math.inf]
        i, j = 0, 0
        q, r = 0, 0
        for k in range(0, n):
            if a[i] < b[j]:
                result[k] = a[i]
                i+=1
            else:
                result[k] = b[j]
                inversionCount += n//2 - i
                j+=1
        return result, inversionCount

    def solveRecursive(self, items):
        self.recursiveCalls += 1
        n = len(items)
        baseCase = []
        if n == 0:
            return baseCase, 0
        if n == 1:
            baseCase.append(items[0]), 0
            return baseCase, 0
        if n == 2:
            if items[0] < items[1]:
                baseCase.append(items[0])
                baseCase.append(items[1])
                return baseCase, 0
            else:
                baseCase.append(items[1])
                baseCase.append(items[0])
                return baseCase, 1
        left, right = self.splitArray(items)
        sortedLeft, countLeft = self.solveRecursive(left)
        sortedRight, countRight = self.solveRecursive(right)
        merged, mergeCount = self.merge(sortedLeft,sortedRight,n)
        return merged, countLeft + countRight + mergeCount
    
    def printRecursiveCalls(self):
        print('CountInversions', self.recursiveCalls)

