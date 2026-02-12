class TwoSum:
    @staticmethod
    def resolve_hash(nums, target):
        vistos = {}
        for index, number in enumerate(nums):
            complement = target - number

            if complement in vistos:
                teste = [vistos[complement], index]
                return teste
            vistos[number] = index

        return []


nums = [2, 3, 1, 3]
target = 6
solution = TwoSum().resolve_hash(nums, target)
print(solution)