'''s=[]



s.append('https://cnn.com/')
s.append('https://cnn.com/world')
s.append('https://cn.com/india')
s.append('https://cnn.com/china')

s.pop()#removes last entry
print(s)

print(s[-1])#gets last element'''

#Write a function in python that can reverse a string using stack data structure.
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
from collections import deque
#stack=deque()
class Stack:
    def __init__(self):
        self.container=deque() #object of deque

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):#returns value but doesnt remove it
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)

'''def reverse_string(stack, string):
        #loop through and push contents
    for i in string:
        stack.push(i)
        
    reverse=''
    while not stack.is_empty:
        reverse+=stack.pop()
            
    return reverse

#stack=Stack()
#string="We will conquere COVID-19"    
#print(reverse_string(stack, string))'''

#Write a function in python that checks if paranthesis in the
#  string are balanced or not. Possible parantheses are "{}',"()" or "[]".
def matched(x,y):
    param_dict={
        '(':')',
        '{':'}',
        '[':']',
    }
    return matched[x]==y

def is_balanced(p):
    stack=Stack()
    for i in p:
        if i=='(' or i=='{' or i=='[':
            stack.push(i)
        if i==')' or i=='}'or i==']':
            if stack.size()==0:
                return False
            if not matched(i, stack.pop()):
                return False
    return stack.size()==0

if __name__ == '__main__':
    print(is_balanced("({a+b})"))




#s=Stack()


