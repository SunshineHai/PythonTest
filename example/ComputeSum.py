# 一、数字求和
# 用户输入数字

num1 = input('请输入第一个数字：');
num2 = input('请输入第二个数字：');

sum = float(num1) + float(num2)


print('数字 {0} 和 {1} 相加的结果为：{2}'.format(num1,num2,sum))  # 占位符
# 或者
print('两数之和为%.1f'%(sum))        # 这种表示方法和 C 语言类似
# 二、Python 平方根
# ** 乘方，使用很方便
num3 = float(input('请输入一个数字'))
num_sqrt = num3 ** 0.5
print('%.3f 的平方根是 %.3f'%(num3,num_sqrt))