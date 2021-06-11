
import cx_Oracle                # 导入cx_Oracle 包，用来连接数据库
# 用户名+密码@数据库IP/数据库名称
conn  = cx_Oracle.connect('yanghk/123456@192.168.31.172:1521/ORCL')

cursor = conn.cursor()
result = cursor.execute('select * from choice')
# 用fetchone() 方法获取一条数据
data = cursor.fetchone()
print(data)

# 使用 fetchall() 获取所有数据
allData = cursor.fetchall()
print(allData)              # 以列表形式输出，每个子元素为元组

# 获取部分数据 fetchmany(8)
manyData = cursor.fetchmany()
print(manyData)
conn.close()
