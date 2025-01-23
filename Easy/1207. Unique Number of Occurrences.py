class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for x in arr:
            if x not in occurrences.keys():
                occurrences[x] = 1
            else:
                occurrences[x] += 1
        seen = []
        points = 0
        for x in occurrences.values():
            if x in seen:
                points += 1
            else:
                seen.append(x)
        if points == 0:
            return True
        else:
            return False
