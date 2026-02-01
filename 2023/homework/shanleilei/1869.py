class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        mo = 0        
        mz = 0
        #遍历s字符串
        for i in range(len(s)):
            #当元素值为1
            if s[i] == "1":
                #初始化局部计数器
                o = 1
                #遍历剩余的元素
                for a in range(len(s)-i-1):
                    #当再次遇到1，增加计数器
                    if s[i+a+1] == "1":
                        o+=1
                    
                    #否则跳出循环
                    else:
                        break
                #如果局部计数器大于外部计数器，则将局部计数器赋值给外部
                if o > mo: mo=o
                print("1的个数:{}".format(mo))
            #如果遇到0
            elif s[i] == "0": 
                #初始化局部计数器
                z = 1
                #遍历剩余的元素
                for d in range(len(s)-i-1):
                    #当再次遇到0，增加计数器
                    if s[i+d+1] == "0":
                        z+=1
                    
                    #否则跳出循环
                    else:
                        break
                #如果局部计数器大于外部计数器，则将局部计数器赋值给外部
                if z > mz: mz=z
                print("0的个数:{}".format(mz))
        print(mo,mz)
        #比较0和1的个数
        return  mo>mz
    
solution = Solution()
s = "1101"

print(solution.checkZeroOnes(s))