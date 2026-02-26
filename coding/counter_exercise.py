from collections import Counter

def counter(nums, k):
    counter = Counter(nums)
    result = counter.most_common(k)
    print(result)

nums = [1, 1, 1, 2, 2, 3]
k = 2
counter(nums, k)