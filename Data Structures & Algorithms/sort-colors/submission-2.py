class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1
        
        k = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                nums[k] = n
                k += 1
        return nums
