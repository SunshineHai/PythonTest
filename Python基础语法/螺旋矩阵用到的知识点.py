print([0])
print([0]*2)
print([0] * 10)
# printf([0] * n) : 表示列表中的元素 为 n个0.

# 浅拷贝 和 深拷贝
# 一维数组：
n = 5
c1 = [0] * n
print(c1)

dp1 = [0 for _ in range(n)] # 深拷贝
print(dp1)
# 二维数组：
# 创建一个3*4的矩阵，元素全为0；
row = 3; column = 4
dp1 = [[0] * 4] * 3
print(dp1)

dp2 = [[0 for _ in range(4)] for _ in range(3)]
print('The result of dp2 is :{0}'.format(dp2))
# 改写：
dp2 = [[0] * column for _ in range(3)]
print(dp2)
# 定义 n 行 n 列 的零矩阵：
n = 4
matrix = [[0] * n for _ in range(n)]
print(matrix)
# 遍历 n的平方次
for i in range(n * n):
    print(i)
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dx, dy = dirs[3]
print(dx, dy)
