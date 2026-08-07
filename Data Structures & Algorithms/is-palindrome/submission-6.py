class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0                  # Start pointer at the beginning of the string
        right = len(s) - 1        # Start pointer at the end of the string

        # Keep checking until the two pointers meet or cross
        while left < right:

            # Move the left pointer forward until it points
            # to a letter or digit.
            #
            # Example:
            # s = "A man, a plan, a canal: Panama"
            #      ^
            # left starts at 'A' -> already alphanumeric, so it stays.
            #
            # Later, if left points to ' ' or ',' or ':',
            # this loop skips over them.
            while left < right and not s[left].isalnum():
                left += 1

            # Move the right pointer backward until it points
            # to a letter or digit.
            #
            # Example:
            #                                   ^
            # right may be at ':'
            # Skip ':' and continue until reaching 'a'.
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the two characters after converting both
            # to lowercase so that uppercase/lowercase are treated
            # as the same.
            #
            # Example:
            # 'A'.lower() == 'a'.lower()
            # 'A' == 'a'  -> True after lowercase conversion
            if s[left].lower() != s[right].lower():
                return False

            # If they matched, move both pointers inward
            # to compare the next pair of characters.
            left += 1
            right -= 1

        # If every pair matched, it is a palindrome.
        return True