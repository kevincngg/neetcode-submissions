class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup = set()
        for i in range(len(nums)):
            nodup.add(nums[i])
        return len(nodup) != len(nums)