class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter +=1
                max_count = max(max_count, counter)
            if nums[i] == 0:
                counter = 0
        return max_count

