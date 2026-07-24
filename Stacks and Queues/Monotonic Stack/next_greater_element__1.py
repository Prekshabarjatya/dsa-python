"""
This module contains the optimal solution for LeetCode 496: Next Greater Element I.
"""
from typing import List

# pylint: disable=too-few-public-methods
class Solution:
    """
    Solution class using a Monotonic Stack to find next greater elements.
    """
    # pylint: disable=invalid-name
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Find the next greater element for each value in nums1 based on nums2.
        """
        # Dictionary to store the next greater element for each number in nums2
        nge_map = {}
        stack = []

        # Process nums2 from right to left to build the next greater element map
        for num in reversed(nums2):
            # Maintain a decreasing stack structure
            while stack and stack[-1] <= num:
                stack.pop()

            # If stack is not empty, the top element is the next greater element
            if stack:
                nge_map[num] = stack[-1]
            else:
                nge_map[num] = -1

            # Push current number onto the stack
            stack.append(num)

        # Build the final result array for elements present in nums1
        result = [nge_map[x] for x in nums1]
        return result