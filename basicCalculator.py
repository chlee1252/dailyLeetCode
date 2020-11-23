class Solution:
    def calculate(self, s: str) -> int:
        num , op , stack = 0, '+', []
        ops ={
        '+': lambda x,y : y,
        '-': lambda x,y: -y,
        '*' : lambda x,y: x*y,
        '/': lambda x,y: int(float(x)/float(y))
            
        }
        s+= '+'
        for c in s:
            if c.isdigit():
                num = num*10+int(c)
            elif c==' ':
                continue
            else:
                prev = 0 if op in '+-' else stack.pop()
                stack.append(ops[op](prev,num))
                num, op = 0, c
    
        print(stack)
        return sum(stack)