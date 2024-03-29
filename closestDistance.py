import math
import copy
class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

class ClosestDistance:

    def dist(self, p1, p2):
        return math.sqrt( ((p1.x-p2.x)*(p1.x-p2.x)) + 
                        ((p1.y - p2.y)*(p1.y - p2.y)) )
                        
    def __init__(self, items):
        self.recursiveCalls = 0
        self.A = sorted(items, key=lambda point: point.x)
        self.B = sorted(items, key=lambda point: point.y)

    def solve(self):
        return self.solveRecursive(self.A, self.B, len(self.A))

    def splitArray(self,arrA,arrB):
        m = len(arrA)//2
        return arrA[:m], arrB[:m], arrA[m:], arrB[m:]
        
    # A Brute Force method to return the
    # smallest distance between two points
    # in P[] of size n
    def bruteForce(self, xy_arr):
        # brute force approach to find closest distance 
        dmin = math.inf
        best = None
        for i, pnt_i in enumerate(xy_arr[:-1]): 
            dis_storage_min = math.inf
            dmin_rec_best = []     
            for pnt_j in xy_arr[i+1:]:
                dis_storage_min = self.dist(pnt_i, pnt_j)   
                if dis_storage_min < dmin:
                    dmin = dis_storage_min  
                    dmin_rec_best = pnt_i, pnt_j
            if dis_storage_min < dmin:
                dmin = dis_storage_min  
                best = pnt_i, pnt_j
        return best, dmin

    def solveRecursive(self, x, y, n):
        self.recursiveCalls += 1
        n = len(x)
        if n == 0:
            raise Exception('n=0')
        # If there are 2 or 3 points, 
        # then use brute force 
        if n <= 3:
            return self.bruteForce(x)

        mid = n//2
        #midPoint = x[mid-1]

        Lx, Ly, Rx, Ry = self.splitArray(x,y)
        l12, bestL = self.solveRecursive(Lx, Ly, mid)
        r12, bestR = self.solveRecursive(Rx, Ry, n - mid)
        bestP = []
        best = math.inf
        if bestL < bestR:
            bestP = l12
            best = bestL
        else:
            bestP = r12
            best = bestR
        s12, bestS = self.merge(Lx, Rx, Ly, Ry, best, bestP, n)
        if bestS < best:
            bestP = s12
            best = bestS
        return bestP, best
    def merge(self, Lx, Rx, Ly, Ry, lr_d, bestP, n):
        midPoint = Lx[len(Lx)-1]
        Sy = []
        leftside = abs(midPoint.x - lr_d) * 2
        for k in range(0, len(Ly)):
            if abs(Ly[k].x - midPoint.x) <= leftside: 
                Sy.append(Ly[k])
        for k in range(0, len(Ry)):
            if abs(Ry[k].x - midPoint.x) <= leftside: 
                Sy.append(Ry[k])
        return self.stripClosest(Sy, bestP, lr_d)
    
    #https://codereview.stackexchange.com/questions/198471/finding-the-closest-pair-of-points-divide-and-conquer/199668#199668
    def stripClosest(self, xy_arr_y_sorted, best, dmin):
        # takes in array sorted in y, and minimum distance of n/2 halves
        # for each point it computes distance to 7 subsequent points
        # output min distance encountered

        dmin_rec = dmin
        dmin_rec_best = best
        if len(xy_arr_y_sorted) == 1:
            return [], math.inf

        if len(xy_arr_y_sorted) > 7:            
            for i, pnt_i in enumerate(xy_arr_y_sorted[:-7]):
                dis_storage_min = math.inf
                dmin_rec_best = []
                for pnt_j in xy_arr_y_sorted[i+1:i+1+7]:
                    dis_storage_min = self.dist(pnt_i, pnt_j)
                    if dis_storage_min < dmin_rec:
                        dmin_rec = dis_storage_min
                        dmin_rec_best = [pnt_i,pnt_j]
                if dis_storage_min < dmin_rec:
                    dmin_rec = dis_storage_min
                    dmin_rec_best = [pnt_i,pnt_j]
        else:
            for k, pnt_k in enumerate(xy_arr_y_sorted[:-1]):    
                dis_storage_min = math.inf
                dmin_rec_best = []
                for pnt_l in xy_arr_y_sorted[k+1:]:
                    dis_storage_min = self.dist(pnt_k, pnt_l)
                    if dis_storage_min < dmin_rec:
                        dmin_rec = dis_storage_min 
                        dmin_rec_best = [pnt_k, pnt_l]
                if dis_storage_min < dmin_rec:
                    dmin_rec = dis_storage_min 
                    dmin_rec_best = dmin_rec_best

        return dmin_rec_best, dmin_rec  