bool checkZeroOnes(char* s) {
    int len;
    len = strlen(s);
    char pre=' ';
    char cur=' ';
    int max1 = 0;
    int max0 = 0;
    int cnt = 0;
    for (int i=0; i<=len; i++) {
        if (i==len) {
            cur = ' ';
        } else {
            cur = s[i];
        }
        if (pre!= s[i]) {
            // 当前字符跟前一个字符不同
            if (pre=='0') {
                if (cnt>max0) {
                    // 更新0字符最大长度
                    max0 = cnt;
                }
            }
            if (pre=='1') {
                if (cnt>max1) {
                    // 更新1字符最大长度
                    max1 = cnt;
                }
            }
            pre = s[i];
            cnt = 1;
        }else {
            cnt++;
        }
    }
    return max1>max0;
}
