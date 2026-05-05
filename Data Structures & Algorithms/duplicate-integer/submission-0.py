class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        unique_elements = set(nums)
        return len(nums) != len(unique_elements)
