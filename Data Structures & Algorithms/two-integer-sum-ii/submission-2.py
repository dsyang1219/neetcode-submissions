class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        right_idx = len(numbers) - 1
        left_idx = 0

        right = numbers[right_idx]
        left = numbers[left_idx]

        while left + right != target:

            if left + right > target:
                right_idx -= 1
                right = numbers[right_idx]
            
            else:
                left_idx +=1
                left = numbers[left_idx]

        
        left_idx = left_idx + 1
        right_idx = right_idx + 1

        return [left_idx, right_idx]




        