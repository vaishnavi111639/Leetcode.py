class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        currnum=0
        currstr=""
        for ch in s:
            if ch.isdigit():
                currnum=currnum*10+int(ch)
            elif ch=='[':
                st.append((currnum,currstr))
                currnum=0
                currstr=""
            elif ch==']':
                num1,prev=st.pop()
                currstr=prev+num1*currstr
            else:
                currstr+=ch
        return currstr
        