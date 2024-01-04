class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        #遍历整个数组
        for i in range(len(arr)-1, -1,-1):
            #当索引对应值大于或等于两边时即为“山峰”
            if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:

                
                return i
        return -1
