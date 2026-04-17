class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
   
        rows = len(matrix) 
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1
        
        while low <= high:
            guess =(low +high)//2

            row = guess // cols
            col = guess % cols

            if matrix[row][col] < target:
                low =guess+1
            
            elif matrix[row][col] > target:
                high =guess-1

            else:
                return True

        return False                
