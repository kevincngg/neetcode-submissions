class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        original_val = 0
        for i in range(len(arr) -1, -1, -1):
            original_value = arr[i]
            arr[i] = right_max
            right_max=max(right_max,original_value)
        arr[len(arr)-1] = -1
        return arr