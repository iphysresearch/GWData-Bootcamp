int countSegments(char * s){
    int len,cnt;
    len = strlen(s);
    cnt = 0;
    //遍历字符串
    for (int i =0; i<len;) {
        // 跳过空格字符
        if (s[i] == ' ') {
            i++;
            continue;
        }else {
            //第一个非空格字符计数+1
            cnt++;
            //跳过后续的非空格字符
            while (s[i] != ' ' && i<len) {
                i++;
            }
        }
    }
    //返回单词数量
    return cnt;
}
