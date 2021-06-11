import collections

class Solution(object):
    def totalFruit(self, tree):
        # ans 存放最大 子序列的长度。
        ans = i = 0
        count = collections.Counter()
        for j, x in enumerate(tree): # j : 表示数组中的下标， x : 表示下标对应的数组的值
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            ans = max(ans, j - i + 1)
        return ans

if __name__ == "__main__":
    tree = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    solution = Solution()
    ans = solution.totalFruit(tree)
    print(ans)
