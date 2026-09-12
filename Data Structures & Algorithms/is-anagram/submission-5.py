class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = Counter(s)
        a2 = Counter(t)
        return a1 == a2