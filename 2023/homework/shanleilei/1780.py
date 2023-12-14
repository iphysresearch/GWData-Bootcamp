class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        conut = sum(
            1 for i in range(len(s)) if s[i] == '1' and (i == 0 or s[i - 1] == '0')
        )
        #判断计数是否大于1
        #大于1则意味着存在不连续结构即01或10
        return conut <= 1
