class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        nums = []
        i = j = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                nums.append(left[i])
                i += 1
            else:
                nums.append(right[j])
                j += 1

        nums.extend(left[i:])
        nums.extend(right[j:])

        return nums