int peakIndexInMountainArray(int* arr, int arrSize) {
    int mid;
    int start = 0;
    int end = arrSize-1;
    while (true) {
        // 二分法查找
        mid = (start + end)/2;
        if (arr[mid]>arr[mid-1] && arr[mid]>arr[mid+1]) {
            return mid;
        }
        // 继续查找mid~end范围
        if (arr[mid]>arr[mid-1] && arr[mid]<arr[mid+1]) {
            start = mid;
            continue;
        }
        // 继续查找start~mid范围
        if (arr[mid]<arr[mid-1] && arr[mid]>arr[mid+1]) {
            end = mid;
            continue;
        }
    }
}
