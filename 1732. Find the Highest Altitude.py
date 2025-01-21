class Solution(object):
    def largestAltitude(self, gain):
        new_list = [0]
        for i in range(0,len(gain)):
            new_list.append(new_list[i] + gain[i])
        return max(new_list)
