class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialise left, right pointers
        left, right = 0, len(s)-1

        # While left < right:
        while left < right:
            # While left < right and left is not alnum
            while left < right and not s[left].isalnum():
                # left to move up
                left += 1

            # While right > left and right is not alnum
            while right > left and not s[right].isalnum():
                # right to move down
                right -= 1

            # Compare left.lower() and right.lower(), if not equals
            if s[left].lower() != s[right].lower():
                return False

            left, right = left + 1, right - 1

        # Return True (no discrepancy)
        return True