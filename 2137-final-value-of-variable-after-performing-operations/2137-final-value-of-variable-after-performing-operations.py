class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for ops in operations:
            if (ops == '++X' or ops == 'X++'):
                x += 1
            elif (ops == '--X' or ops == 'X--'):
                x -= 1
        return x
        