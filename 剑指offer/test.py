def findNumberIn2DArray(matrix, target: int) -> bool:
    if not matrix: return False
    rows, cols = len(matrix[0]), len(matrix)
    if rows * cols == 0: return False
    c, r = 0, rows - 1
    while r >= 0 and c < cols:
        if matrix[c][r] < target:
            c += 1
        elif matrix[c][r] > target:
            r -= 1
        else:
            return True
    return False
findNumberIn2DArray([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],
20)