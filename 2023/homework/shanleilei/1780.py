class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        conut = 0
        #设置计数
        for i in range(len(s)) :#遍历字符串
            if s[i] == '1' and (i == 0 or  s[i-1] == '0') :
                #如果s的第一位等于1 或者1的前一位是0，则计数加一。
                conut += 1
        #判断计数是否大于1
        #大于1则意味着存在不连续结构即01或10
        if conut > 1:
            return False
        return True
