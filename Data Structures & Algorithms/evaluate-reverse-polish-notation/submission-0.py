class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for i in range(len(tokens)):
             if tokens[i] not in ["+", "-", "*", "/"]:
                st.append(int(tokens[i]))

             else:
                b = st.pop()
                a = st.pop()   

                if tokens[i] == '+':
                  res = a + b
                  st.append(res)

                elif tokens[i] == '-':
                    res =a -b
                    st.append(res)  

                elif tokens[i] == '*':
                    res =a *b
                    st.append(res) 

                elif tokens[i] == '/':
                    res = int(a /b)
                    st.append(res)         

        return st[-1]           

  


        