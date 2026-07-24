"""
This module contains the optimal solution for LeetCode 503: Next Greater Element II.
"""
from typing import List

# pylint: disable=too-few-public-methods
class Solution:
    """
    Solution class using a Monotonic Stack with circular array mapping.
    """
    # pylint: disable=invalid-name
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Find the next greater element for all values in a circular array.
        Time Complexity: O(N) | Space Complexity: O(N)
        """
        n = len(nums)
        result = [-1] * n
        stack = []

        # Process virtually across a doubled array length (2N-1 down to 0)
        for i in range(2 * n - 1, -1, -1):
            actual_index = i % n
            num = nums[actual_index]

            # Maintain a decreasing stack structure
            while stack and stack[-1] <= num:
                stack.pop()

            # Assign directly to the slot during the real pass phase
            if i < n:
                if stack:
                    result[actual_index] = stack[-1]
                else:
                    result[actual_index] = -1

            # Push current number onto the stack
            stack.append(num)

        return result
    