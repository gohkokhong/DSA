class Solution:
    def isPalindrome(self, s: str) -> bool:        
        # Initialise a new string
        cleanedStr = ''

        # Iterate through the string
        for char in s:
            # If the char isalnum:
            if char.isalnum():
                # Add into the string as lower case
                cleanedStr += char.lower()

        # Return string and reversed
        return cleanedStr == cleanedStr[::-1]