class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l = 0
        maxi = 0

        for r in range(len(s)):

            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            maxi = max(maxi, r - l + 1)

        return maxi