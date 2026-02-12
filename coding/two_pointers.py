class TwoSum:
    @staticmethod
    def validate(target, nums):
        left_position = 0
        right_position = len(nums) - 1

        while left_position < right_position:
            if nums[left_position] + nums[right_position] == target:
                return [left_position, right_position]

            if nums[left_position] + nums[right_position] > target:
                right_position -= 1

            elif nums[left_position] + nums[right_position] < target:
                left_position += 1

        return None

nums = [1, 3, 4, 5, 7, 10]
target = 9
two_sum = TwoSum()
print(two_sum.validate(target, nums))
