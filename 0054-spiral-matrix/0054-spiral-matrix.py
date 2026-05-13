class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        
        result = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 1. Move Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1
            
            # 2. Move Down
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1
            
            # 3. Move Left (Check needed to ensure we still have a row)
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            # 4. Move Up (Check needed to ensure we still have a column)
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1
                
        return result