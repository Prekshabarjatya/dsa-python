class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
                n = len(nums)
                result = [-1] * n
                stack = []

                # Process nums from right to left to build the next greater element map
                for i in range (2*n-1,-1,-1):
                    num = nums[i%n]
                    # Maintain a decreasing stack structure
                    while stack and stack[-1] <= num:
                        stack.pop()

                    # If stack is not empty, the top element is the next greater element
                    if i < n :
                        if stack:
                            result[i%n] = stack[-1]
                        else:
                            result[i%n] = -1

                    # Push current number onto the stack
                    stack.append(num)

                # Build the final result array for elements present in nums1
                return result