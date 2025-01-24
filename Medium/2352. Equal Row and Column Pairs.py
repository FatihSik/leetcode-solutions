class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        counter = 0
        for i in range(len(grid)):
            columns.append([row[i] for row in grid])
        for column in columns:
            if column in grid:
                x = grid.count(column)
                counter += x
        return counter
