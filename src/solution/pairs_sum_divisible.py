from collections import defaultdict


class Solution:

    def count_divisible_pairs(self, input_values: [int], divider: int):
        reminder_counts = defaultdict(int)

        for number in input_values:
            reminder = number % divider
            reminder_counts[reminder] += 1

        divisible_pairs_count = 0
        for number in input_values:
            reminder = number % divider
            # e.g. we have 9 and 12 and divider is 3, in this case reminder will be 0
            # the complementary reminder shouldn't be 3 - 0 = 3, as for both 9 and 12 extra reminder is not needed
            complementary_reminder = divider - reminder if reminder != 0 else 0
            divisible_pairs_count += reminder_counts[complementary_reminder]

            if reminder == complementary_reminder:
                divisible_pairs_count -= 1

        # we divide it to two because we count each pair twice
        # e.g. when we have pair 1 and 2 and the divider is 3 we count 1 and 2 then we count 2 and 1
        return divisible_pairs_count // 2