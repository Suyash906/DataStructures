# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end  =1, n
        while start < end:
            mid = (start+end) //2
            if not isBadVersion(mid):
                if isBadVersion(mid+1):
                    return (mid+1)
                else:
                    start = mid+1
            elif isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return (mid)
                else:
                    end = mid-1
        return 1