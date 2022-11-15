# 1
# Вывести индексы чисел из списка, при сложении будет target: [1,2,3,4], 6 = (1,3)

def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return (x, y)

# 2
#
