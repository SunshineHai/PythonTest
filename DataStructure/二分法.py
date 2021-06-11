


# 前提有序的数组 [left, right] 都是左闭右闭，找到则返回第一个下标，否则返回 -1.
def dichotomy(nums : list, target : int) -> int:
    n = len(nums)-1 # 数组中最后一个元素下标
    left, right = 0, n
    while left <= right:
        # 求中间的 middle 值，与目标值进行比较
        middle = (left + right) // 2
        if nums[middle] == target:
            return nums[middle]
        elif nums[middle] < target:	# 目标值在右半部分
            left = middle + 1
        else:						# 目标值在左半部分
            right = middle-1        # 可以减1也可以不减1
    # 数组中没有target元素；1.若target < nums[0]，则插入位置的下标为0
    # 2.如果target > 最后一个元素，则插入到最后。
    return 0 if target < nums[0] else n


nums = [1, 3, 5, 6, 10, 14, 19, 26]
print("-----------")
print(dichotomy(nums, 10))
