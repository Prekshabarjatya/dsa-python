class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nge_map = {}
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                nge_map[num] = stack[-1]
            else:
                nge_map[num] = -1

            stack.append(num)

        result = [nge_map[x] for x in nums1]
        return result

    
