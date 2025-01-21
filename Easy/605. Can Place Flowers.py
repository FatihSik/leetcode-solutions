class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        emptySpace = 1
        availableSpace = 0
        for i in flowerbed:
            if i == 1:
                emptySpace = 0
            else:
                emptySpace +=1
                if emptySpace == 3:
                    availableSpace +=1
                    emptySpace = 1
        if emptySpace == 2:
            availableSpace += 1
        return availableSpace >= n
