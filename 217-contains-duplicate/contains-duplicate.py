class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        for num in nums:
            if num in checker:
                return True

            checker.add(num)

        return False