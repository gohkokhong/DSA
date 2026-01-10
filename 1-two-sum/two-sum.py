class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a copy of the array and sort it in asc order
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        A.sort()

        # Initialise two pointers
        i = 0
        j = len(nums) - 1

        # Iterate through the array with the two pointers, and check if the sum of the two numbers equal to the target
        while i < j:
            cur = A[i][0] + A[j][0]

            # If the sum is equal to the target, return the indices of the two numbers
            if cur == target:
                return [min(A[i][1], A[j][1]),
                        max(A[i][1], A[j][1])]

            # If the sum is less than the target, move the left pointer to the right, which will increase the sum.
            elif cur < target:
                i += 1

            # If the sum is greater than the target, move the right pointer to the left, which will decrease the sum
            else:
                j -= 1

        # There is guaranteed to be exactly one solution, so we will never return an empty array.
        return []

