
class Solution:
    # s : 母串 ; t : 子串
    def minWindow(self, s : str, t : str) -> str:
        start, end = 0, 0
        countDic = {}
        ansL, ansR = -1, -1
        length = len(s)
        for end, j in enumerate(s):
            # countDic : 存放中间字符串
            if countDic.get(j) == None:
                countDic[j] = 1
            else:
                countDic[j] += 1
            # 把字串 t 转化成字典 dictT
            dictT  = Solution().strToDic(t)
            isFlag = Solution().subInStr(dictT, countDic)
            while isFlag:
                # 1.判断 若字串 t 在 中间字符串countDict中，下面if语句记录截取最短的字符串
                if(end-start+1 <= length):
                    length = end - start + 1
                    ansL = start
                    ansR= start + length
                # start对应的当前字符
                ch = s[start]
                if dictT.get(ch) == None:
                    if countDic.get(ch) != None:
                        del countDic[ch]
                elif countDic.get(ch) > 1:
                    countDic[ch] = countDic.get(ch) - 1
                else:
                    del countDic[ch]
                isFlag = Solution().subInStr(dictT, countDic)
                start += 1
        return '' if ansR == -1 else s[ansL: ansR]
    # 判断字串subStr 是否在countDic中
    def subInStr(self, subStr, countDic) -> bool:
        for key, value in subStr.items():
            if countDic.get(key) == None:
                return False
            elif countDic.get(key) < value:
                return False
        return True
    # 把 字符串 转化为 字典
    def strToDic(self, s : str):
        strDic = {}
        for j in s:
            if strDic.get(j) == None:
                strDic[j] = 1
            else:
                strDic[j] += 1
        return strDic

s = "a"
t = "acc"
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"

if __name__ == "__main__":
    s = 'ADOBECODEBANC'
    t = "ABC"
    solution = Solution()
    ans = solution.minWindow(s, t)
    print('字串为:{0}'.format(ans))

