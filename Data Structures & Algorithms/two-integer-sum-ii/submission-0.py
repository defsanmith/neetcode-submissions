class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        j = len(numbers) - 1

        while i < j:
            k = numbers[i] + numbers[j]

            if k == target:
                return [i + 1, j + 1]

            if k < target:
                i += 1
            else:
                j -= 1
        