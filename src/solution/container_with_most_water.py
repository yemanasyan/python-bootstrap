from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_container_volume = 0
        start = 0
        end = len(height) - 1

        while start < end:
            volume = (end - start) * min(height[start], height[end])
            max_container_volume = max(max_container_volume, volume)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_container_volume
