class Solution(object):
    def mergeAlternately(self, word1, word2):
        listWord1 = list(word1)
        listWord2 = list(word2)
        newList = []
        ticker = 0
        for i in range(min(len(listWord1), len(listWord2))):
            newList.append(listWord1[i])
            newList.append(listWord2[i])
            ticker = i
        if len(listWord1) > len(listWord2):
            for i in range(ticker + 1, len(listWord1)):
                newList.append(listWord1[i])
        else:
            for i in range(ticker + 1, len(listWord2)):
                newList.append(listWord2[i])
        
        string = ''
        for i in newList:
            string += i

        return string
        
