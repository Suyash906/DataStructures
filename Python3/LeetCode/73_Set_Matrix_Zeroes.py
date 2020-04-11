class Solution:
    def markZeroTop(self, matrix, i, j):
        while i >= 0:
            if 0 != matrix[i][j]:
                matrix[i][j] = -1000000
            i = i - 1
        return matrix
    
    def markZeroLeft(self, matrix, i, j):
        while j >= 0:
            if 0 != matrix[i][j]:
                matrix[i][j] = -1000000
            j = j -1
        return matrix
    
    def markZeroBottom(self, matrix, i, j):
        rowSize = len(matrix)
        while i < rowSize:
            if 0 != matrix[i][j]:
                matrix[i][j] = -1000000
            i = i + 1
        return matrix
    
    def markZeroRight(self, matrix, i, j):
        colSize = len(matrix[0])
        while j < colSize:
            if 0 != matrix[i][j]:
                matrix[i][j] = -1000000
            j = j + 1
        return matrix
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i,currList in enumerate(matrix):
            for j,currValue in enumerate(currList):
                if -1000000 == currValue:
                    matrix[i][j] = 0
                elif 0 == currValue:
                    matrix = self.markZeroLeft(matrix, i, j-1)
                    matrix = self.markZeroTop(matrix, i-1, j)
                    matrix = self.markZeroRight(matrix, i, j+1)
                    matrix = self.markZeroBottom(matrix, i+1, j)
        for i,currList in enumerate(matrix):
            for j,currValue in enumerate(currList):
                if currValue == -1000000:
                    matrix[i][j] = 0