class SlidingWindow:
    def max_sum_subarray(self, nums: list[int], k: int) -> int:
        window_sum = sum(nums[0:k])
        max_sum = window_sum

        # 2. Desliza a janela
        for i in range(1, len(nums) - k + 1):
            # Remove o que saiu, adiciona o que entrou
            window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, window_sum)

        return max_sum

    def maximum_vowels(self, nums, k):
        hashmap = {}
        for i, num in enumerate(nums):
            if num == hashmap.get(num):
                 hashmap[num] = 1
        return


s = "abciiidef"
k = 1
sliding_window = SlidingWindow()
sliding_window.maximum_vowels(s, k)

