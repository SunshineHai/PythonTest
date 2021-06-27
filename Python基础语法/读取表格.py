print('hello')


import pandas as pd
df = pd.read_csv('ex1.csv')
print(df)

def dichotomy(arr : list, ele : int) -> int:
    print(arr, ele)
    left, right = 0, len(arr) - 1
    while(left <= right):
        mid = (left + right) // 2
        if arr[mid] == ele:
            return mid
        elif arr[mid] > ele:
            right = mid - 1
        else:
            left = mid + 1
    return -1

arr, ele = [2, 4, 7, 8, 10, 16, 20], 10
res = dichotomy(arr, ele)
print(res)