class SlidingWindow:
    def max_sum_subarray(self, nums: list[int], k: int) -> int:
        for num in nums:
            print(num)


nums = [2, 1, 5, 1, 3, 2]
k = 1
sliding_window = SlidingWindow()
sliding_window.max_sum_subarray(nums, k)

