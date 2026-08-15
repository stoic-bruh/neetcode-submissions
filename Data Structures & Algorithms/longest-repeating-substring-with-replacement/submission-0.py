class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_freq = 0
        answer = 0

        for right in range(len(s)):

            # Add the new character to the window
            count[s[right]] = count.get(s[right], 0) + 1

            # Highest frequency of any character in the window
            max_freq = max(max_freq, count[s[right]])

            # Number of characters we would need to replace
            window_length = right - left + 1
            replacements = window_length - max_freq

            # Window is invalid -> shrink it
            if replacements > k:
                count[s[left]] -= 1
                left += 1

            # Record the largest valid window
            answer = max(answer, right - left + 1)

        return answer