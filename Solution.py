class Solution(object):
    def nCr(self, n, r) :
        res = 1
        for r in range(1, r+1):
            res = (res*(n-r))/r
        return res
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.nCr(m+n-1,m-1)
