import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0
        while l <= r:

            mid = (l+r) // 2
            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            if total_hours > h:
                l = mid + 1
            elif total_hours <= h:
                r = mid - 1
                res = mid
        return res


        