#binary search
#algoritmo de busca que descarta metade dos dados em cada passo, so funciona em dados ordenados

def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        if nums[mid] == target:
            return mid

    return -1


nums = [1, 3, 5, 7, 9, 11, 13]
target = 11

result = binary_search(nums, target)
print(result)