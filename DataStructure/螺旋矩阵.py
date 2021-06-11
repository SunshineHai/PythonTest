

class Solution:
    def generateMatrix(self, n: int):
        # dirs : 用来控制赋值时方向的改变；(0, 1) : 代表 向右旋转，(1, 0) : 向下旋转， (0, -1) : 向左旋转；（-1，0） ： 向上旋转
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 定义列表 dirs，里面包含四个元组，可以看成是一个坐标点
        # 右、下、左、上
        # 定义 n 行 n 列 的元素都为0 的矩阵：
        matrix = [[0] * n for _ in range(n)]
        row, col, dirIdx = 0, 0, 0  # row : 行标， col:列标
        for i in range(n * n):
            matrix[row][col] = i + 1
            dx, dy = dirs[dirIdx]
            r, c = row + dx, col + dy   # r、n ：下一个元素的行号 和 列号
            # 下面的if语句，用来判断赋值到n维数组的"角"时，该往哪里旋转。
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                dirIdx = (dirIdx + 1) % 4  # 顺时针旋转至下一个方向
                dx, dy = dirs[dirIdx]
            row, col = row + dx, col + dy

        return matrix

if __name__ == "__main__":
    solu = Solution()
    ans = solu.generateMatrix(3)
    print(ans)

# 1.初始化 n x n 的零矩阵 matrix[n][n]。
# 2.给 matrix[i][j] 赋值，如果上、下、左、右赋值到头了，或者下一个元素不为零（说明下个元素已经赋值过了）。
# 3.继续循环第二步，继续赋值。