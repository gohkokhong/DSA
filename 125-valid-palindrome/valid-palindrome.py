class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Initialise two pointers
        left, right = 0, len(s)-1

        # While left is less than r:
        while left < right:
            # Move left forward until it points to an alphanumeric char
            while left < right and not s[left].isalnum():
                left += 1
            # Move right backward until it points to an alphanumeric char
            while right > left and not s[right].isalnum():
                right -= 1

            # Compare the lower case chars at left and right
            if s[left].lower() != s[right].lower():
                # If they don't match, return False
                return False

            # Move both pointers inward l += 1, r -= 1
            left, right = left + 1, right - 1

        # If loop finishes without mismatch, return True
        return True