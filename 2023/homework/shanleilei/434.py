
class Solution:
    def countSegments(self, s: str) -> int:
            #使用Spilt分割句子，并使用len测出分割后的单词数组长度
            return len(s.split())
