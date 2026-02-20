class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strings have length mismatch
        if len(s) != len(t):
            return False

        # Initialise dictionaries
        sDict, tDict = {}, {}

        for index in range(len(s)):
            sDict[s[index]] = 1 + sDict.get(s[index], 0)
            tDict[t[index]] = 1 + tDict.get(t[index], 0)

        if sDict == tDict:
            return True

        return False