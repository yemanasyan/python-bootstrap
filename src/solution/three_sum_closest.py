from typing import List
import sys

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest_summary = sys.maxsize
        closest_distance = sys.maxsize

        for i in range(len(nums) - 2):
            j = i + 1
            z = len(nums) - 1

            while j < z:
                summary = nums[i] + nums[j] + nums[z]
                current_distance = abs(summary - target)
                if current_distance < closest_distance:
                    closest_summary = summary
                    closest_distance = current_distance

                if summary > target:
                    z = z - 1
                else:
                    j = j + 1

        return closest_summary
