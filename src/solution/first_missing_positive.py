class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for index in range(len(nums)):
            self.sort_nth_element(index, nums)

        for index, num in enumerate(nums):
            if num is None:
                return index + 1

        return len(nums)

    def sort_nth_element(self, index: int, nums: list[int]):
        if nums[index] is None or nums[index] == index + 1:
            return

        if 0 < nums[index] <= len(nums) and \
                (nums[index] == index + 1 or nums[nums[index] - 1] != nums[index]):
            nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
            self.sort_nth_element(index, nums)
        else:
            nums[index] = None
