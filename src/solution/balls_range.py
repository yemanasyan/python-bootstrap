class Solution:
    # https://stackoverflow.com/questions/42678358/whats-the-faster-algorithm-to-rearrange-given-array-of-numbers
    # https://app.codesignal.com/live-interview/FsDeTafpTEEeQZXwL
    def min_moves(self, balls: list) -> int:
        balls.sort()
        balls_length = len(balls)
        max_balls_in_range = 0
        start_ball_index = 0

        for last_ball_index, last_ball_value in enumerate(balls):
            start_ball_value = last_ball_value - balls_length + 1
            while balls[start_ball_index] < start_ball_value:
                start_ball_index += 1

            max_balls_in_range = max(max_balls_in_range, last_ball_index - start_ball_index + 1)

        return balls_length - max_balls_in_range
