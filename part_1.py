# 1
# Вывести индексы чисел из списка, при сложении будет target: [1,2,3,4], 6 = (1,3)
def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[x] + nums[y] == target:
                return (x, y)


# 2
# Проверка на полиндромность числа
def isPalindrome(x):
    middle = len(str(x)) // 2
    a = str(x)[:middle]
    if len(str(x)) % 2 > 0:
        middle += 1
    b = str(x)[middle:]
    if a == b[::-1] or len(str(x)) == 1:
        return True
    else:
        return False


# 3
# Вывести поторяющиеся символы
def longestCommonPrefix(strs):
    l = list(zip(*strs))
    prefix = ""
    for i in l:
        if len(set(i)) == 1:
            prefix += i[0]
        else:
            break
    return prefix


print(longestCommonPrefix(["cir", "car"]))
