class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            found = -1
            for j in range(1, len(nums)):
                index = (i+j)%len(nums)
                if nums[index] > nums[i]:
                    found = nums[index]
                    break
            ans.append(found)

        return ans