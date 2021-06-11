# 给定一个数组，求和 >= target 的个数最小的子数组
class Solution:

    def getMinSubArray(self, array, target : int) -> int:
        # array 为空，返回0
        if not array:
            return 0
        start, end = 0, 0
        sum, ans = 0, len(array)+1
        while end < len(array):
            sum += array[end]
            while sum >= target:
                ans = min(ans, end-start+1)
                sum -= array[start]
                start += 1
            end += 1
        return 0 if ans == len(array)+1 else ans

if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    solution = Solution()
    ans = solution.getMinSubArray(nums, 7)
    print(ans)
