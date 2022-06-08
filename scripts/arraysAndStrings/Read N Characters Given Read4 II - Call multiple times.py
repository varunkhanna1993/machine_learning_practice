class Solution:
    def __init__(self):
        self.arr=[]
        self.used=False
    def read(self, buf, n: int) -> int:
        copied_chars=0
        read_chars=4
        
        if not self.used:#Grab everything in the first call
            self.used=True
            while read_chars==4:
                buf4=['']*4
                read_chars=read4(buf4)
                self.arr.extend(buf4)
                
        while copied_chars<n and self.arr:
            buf[copied_chars]=self.arr.pop(0)
            copied_chars+=1
                
        
        return copied_chars

Solution().read()