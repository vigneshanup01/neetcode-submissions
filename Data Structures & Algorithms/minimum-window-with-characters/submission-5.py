from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)               # Frequency of every character required from t
        window = Counter()              # Frequency of characters inside our current window

        satisfied = 0                   # Number of distinct characters whose required frequency is satisfied
        required = len(need)            # Number of distinct characters we need to satisfy

        left = 0                        # Left boundary of our sliding window

        bestStart = 0                   # Starting index of the smallest valid window found
        bestLength = float("inf")       # Start with infinity because we haven't found any valid window yet

        for right in range(len(s)):     # Expand the window by moving right

            window[s[right]] += 1       # Add the current character to our window

            # If this character is required AND we have now reached exactly
            # the frequency required by t, one requirement is satisfied
            if s[right] in need and window[s[right]] == need[s[right]]:
                satisfied += 1

            # Once every required character has the required frequency,
            # the current window is valid. Now try to make it smaller.
            while satisfied == required:

                windowLength = right - left + 1   # Calculate current window size

                # If this valid window is smaller than our previous best,
                # save its starting position and length
                if windowLength < bestLength:
                    bestLength = windowLength
                    bestStart = left

                leftChar = s[left]                 # Character we're about to remove
                window[leftChar] -= 1              # Remove it from the window

                # If this character was required AND removing it caused
                # its count to fall below what t requires, the window
                # is no longer satisfying that requirement
                if leftChar in need and window[leftChar] < need[leftChar]:
                    satisfied -= 1

                left += 1                          # Shrink the window from the left

        # If bestLength is still infinity, no valid window was found
        if bestLength == float("inf"):
            return ""

        # Return the smallest valid substring using its start index and length
        return s[bestStart:bestStart + bestLength]