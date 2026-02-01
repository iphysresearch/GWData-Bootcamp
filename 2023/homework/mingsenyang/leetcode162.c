int findPeakElement(int* nums, int numsSize) {
    int start =0;
    int end=numsSize-1;
    int mid;
    while (start<end) {
        // 二分法查找
        mid = (start + end) /2;
        // 更新end值
        if (nums[mid] > nums[mid+1]) {
            end = mid;
        } else {
            // 更新start值
            start = mid+1;
        }
    }
    return start;
}
