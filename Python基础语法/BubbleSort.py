


# 这个不能算做冒泡排序：
# 1.从第1元素，遍历一次找到最小的元素放在第1个元素位置。
# 2.从第2个元素开始，再遍历一次找到最小的元素放到第2个位置。
# 3.从第i个元素开始，再遍历一次，找到最小的元素放到第i个位置。
def bubbleSort(array : list):
    for i in range(0, len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array

newList = [2, 1, 8, 9, 0,3]
print('newList:', bubbleSort(newList))
# 冒泡排序：假如一共 i 个数，进行排序：因为数组是从0开始排序的，所以：i-1 表示数组的最后一个数对应的索引。
# 1.从后往前扫描，找到一个最小的数，然后把它放到第1位；
# 2.从后往前扫描，找到一个次小的数，然后把它放到第2位；
# ......
# i-2.从后往前扫描，找到一个最小的数，然后把它放到第i-2位。
# 只需要冒泡到第 i-2 步，就可以实现排序。
def bubbleSort2(array : list):
          # 若放到这里，j 的值改变了，结果不对
    for i in range(0, len(array)):
        print('i = {0}'.format(i))
        j = len(array) - 2
        while j >= i:
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
            j -= 1
    return array

myList = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print('冒泡:', bubbleSort2(myList))

print('结束......')