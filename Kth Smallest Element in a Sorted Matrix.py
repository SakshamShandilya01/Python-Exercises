class Solution(object):
    def kthSmallest(self, matrix, k):
        a=[]
        for i in matrix:
            a.extend(i)
        a.sort()
        return a[k-1]