# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dimension = binaryMatrix.dimensions()
        row = dimension[0]
        col = dimension[1]
        mincol = col+1
        for i in range(row):
            start = 0
            end = col -1
            while start <= end:
                mid = (start+end) // 2
                if binaryMatrix.get(i,mid) == 1:
                    if mid ==0:
                        return 0
                    elif mid !=0 and binaryMatrix.get(i,mid-1) == 0:
                        mincol = min(mincol,mid)
                        break
                    else:
                        end = mid -1
                else:
                    start = mid+1
        
        return -1 if (col+1 == mincol) else mincol