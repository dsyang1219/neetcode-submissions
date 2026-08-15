from collections import Counter

class Solution:
    counts = {}

    def isAnagram(self, s: str, t: str) -> bool:
        counts_s = {}
        counts_t = {}
        for ch in s:
            counts_s[ch] = counts_s.get(ch, 0) + 1
        for ch in t:
            counts_t[ch] = counts_t.get(ch, 0) + 1
        
        return counts_s == counts_t
