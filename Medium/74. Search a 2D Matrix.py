class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        entries = []
        for row in matrix:
            entries += row
        if target in entries:
            return True
        return False

# beats 100% apparently (doubt it)
