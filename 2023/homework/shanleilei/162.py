class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        #设置左右指针
        left = 0
        right = len(nums)-1

        #循环直至左右指针相遇
        while left < right:
            #设置中间位置
            mid = (left+right)//2
            curr = nums[mid]
            #如果中间值大于右边，则峰值在左半边
            if curr > nums[mid+1]:
                #向左移动右指针
                right = mid
            #否则峰值在右半边
            else:
                #向右移动左指针
                left = mid+1
        
        return left