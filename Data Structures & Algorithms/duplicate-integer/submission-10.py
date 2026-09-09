class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup= set(nums)
        if len(nums) != len(nodup):
            return True
        return False