class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        for i in digits:
            string += f'{i}'
        output = str(int(string) + 1)
        return [int(x) for x in list(output)]
