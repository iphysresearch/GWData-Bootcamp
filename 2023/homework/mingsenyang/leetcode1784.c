bool checkOnesSegment(char* s) {
    int len;
    len = strlen(s);
    int i=0;
    int cnt =0;
    while (i<len) {
        if (s[i]=='1') {
            // 连续的1字符个数+1
            cnt++;
            // 超过2个直接返回
            if (cnt>=2) {
                return false;
            }
            while (i<len && s[i]=='1') {
                i++;
            }
        }else {
            i++;
        }
    }
    return true;
}
