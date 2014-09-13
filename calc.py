#coding=utf8
import stack

class Calc(object):
    def __init__(self):
        self._operator=['+','-','*','/']
        self._proceed={'(':0,'+':1,'-':1,'*':2,'/':2}
    
    def eval(self,expression):
        s=stack.Stack()
        postfix=self.infix2postfix(expression)
        for char in postfix:
            if char.isnumeric():
                s.push(char)
            else:
                a=int(s.pop())
                b=int(s.pop())
                if char == '+':
                    s.push(a+b)
                elif char == '-':
                    s.push(b-a)
                elif char == '*':
                    s.push(b*a)
                else:
                    s.push(b/a)
        return s.pop()
    
    def infix2postfix(self,expression):
        s0=stack.Stack()
        s1=[]
        for char in expression:
            if s0.isEmpty() and char in self._proceed.keys():  # 运算符遇到空栈，则入栈
                s0.push(char)
                continue
            if char.isnumeric(): #数字则直接输出
                s1.append(char)
                continue
            elif char in self._operator:  # 操作符，与栈顶比较，高则入栈，低则压出栈顶，直到高
                while self._proceed[char] <= self._proceed[s0.peek()]:
                    s1.append(s0.pop())
                    if s0.isEmpty():
                        s0.push(char)
                        break
                else:
                    s0.push(char)
                continue
            elif char=='(': # (直接入栈
                s0.push(char)
                continue
            elif char==')': # )压出栈顶直到(，并弃(
                while s0.peek() != '(':
                    s1.append(s0.pop())
                else:
                    s0.pop()
                continue
            else: #非法输入
                print('invalid char')
                
        while not s0.isEmpty():  # 将剩余元素出栈
                s1.append(s0.pop())
        return s1
                
if __name__ == '__main__':
    calc=Calc()
    print(calc.eval(r'5+9-4*2/1/4+((1+2)*4+8)-3/3-1'))