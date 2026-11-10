class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS,COLS = len(matrix), len(matrix[0])
        low,high = 0,ROWS-1
        while low<=high:
            mid = (low + high)//2
            if target > matrix[mid][-1]:
                low = mid +1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                break
        if not low<=high:
            return False
        mid = (low+high)//2
        top, bot = 0, COLS-1
        while top<=bot:
            inner_mid = (top+bot)//2
            if target > matrix[mid][inner_mid]:
                top = inner_mid+1
            elif target < matrix[mid][inner_mid]:
                bot = inner_mid-1
            else:
                return True
        return False