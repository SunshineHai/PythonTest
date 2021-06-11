def strToDic(str: str):
    strDic = {}
    for j in str:
        if strDic.get(j) == None:
            strDic[j] = 1
        else:
            strDic[j] += 1
    return strDic

ans = strToDic('abcdeda')
print(ans)

midDict = {1 : 'A', 2 : 'B', 8 : 'R', 0 : 'U'}
print(midDict)
del midDict[2]
print(midDict)
print(midDict.get(2))

midDict = {'A' : 1, 'B' : 2}
midDict['A'] = midDict.get('A') + 1
print(midDict['A'])


# 判断字串subStr 是否在countDic中
def subInStr(subStr, countDic) -> bool:
    for key, value in subStr.items():
        if countDic.get(key) == None:
            return False
        elif countDic.get(key) < value:
            return False
    return False
dict1 = {'a' : 1, 'b' : 1, 'c': 1}
dict2 = {'a' : 1}
print(subInStr(dict1, dict2))

s = "ABCDEF"
print(s[1:2])
del dict1['a']
print(dict1)

s = 'defefgegeABabceCiopoiooppp'
print(s[0])
print(s[1:])

x = "I love China!    " \
    "我爱中国！   "
print(x)
print(x.rstrip())

