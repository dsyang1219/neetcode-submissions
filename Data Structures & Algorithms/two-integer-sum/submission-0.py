class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        output = []

        for i, num in enumerate(nums):
            needed = target - nums[i]
            if needed in seen:
                output.append(seen.get(needed))
                output.append(i)
                return output
            else:
                seen[nums[i]] = i