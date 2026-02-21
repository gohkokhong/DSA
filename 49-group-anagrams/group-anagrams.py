class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a hashmap to group words
        freqMap = defaultdict(list)

        # Iterate word of strs
        for word in strs:
            # Initialise list for 26 char count
            count = [0] * 26    # [0, 0, 0, ... 0]

            # Iterate char of word
            for char in word:
                # Convert char to an index, and increment hashmap
                count[ord(char) - ord("a")] += 1

            # Append list (updated counts) to hashmap and append corresponding string
            freqMap[tuple(count)].append(word)

        # Return hashmap values
        return list(freqMap.values())