class Solution(object):
    def reverseVowels(self, s):
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowelsList = []
        output = list(s)
        for i in enumerate(list(s)):
            if i[1].lower() in vowels:
                vowelsList.append(i)
        for i in range(len(vowelsList)):
            output[vowelsList[-(i+1)][0]] = vowelsList[i][1] 

        return ''.join(str(x) for x in output)
