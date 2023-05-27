from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        index = -1

        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                index = middle
                break
            elif nums[middle] > target:
                end = middle - 1
            else:
                start = middle + 1

        if index == -1:
            return [-1, -1]

        start_index = index
        while start_index - 1 >= 0 and nums[start_index - 1] == target:
            start_index -= 1

        end_index = index
        while end_index + 1 < len(nums) and nums[end_index + 1] == target:
            end_index += 1

        return [start_index, end_index]