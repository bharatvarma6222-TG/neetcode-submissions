class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            # Check if the value we need exists in our memory
            needed = target - value
            if needed in seen:
                return [seen[needed], i]
            # Otherwise, remember this value and its index
            seen[value] = i