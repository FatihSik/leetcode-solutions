class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        maxVowels = 0
        currentVowelCount = sum(1 for i in range(k) if s[i] in vowels)
        
        maxVowels = currentVowelCount
        
        for i in range(k, len(s)):
            if s[i] in vowels:
                currentVowelCount += 1
            if s[i - k] in vowels:
                currentVowelCount -= 1
            
            maxVowels = max(maxVowels, currentVowelCount)

        return maxVowels
