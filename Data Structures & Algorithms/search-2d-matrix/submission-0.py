class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        top,bottom = 0,ROWS-1
        while top <=bottom:
            mid_row = (top + bottom)//2
            if matrix[mid_row][0]<=target and matrix[mid_row][-1]>=target:
                l,r = 0, len(matrix[mid_row]) - 1
                while l <=r:
                    cur_mid = (l + r)//2
                    if target > matrix[mid_row][cur_mid]:
                        l = cur_mid+1
                    elif target < matrix[mid_row][cur_mid]:
                        r = cur_mid-1
                    else:
                        return True
                return False
            elif matrix[mid_row][0] > target:
                bottom = mid_row-1
            else:
                top = mid_row + 1
        return False