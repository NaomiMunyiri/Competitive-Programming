#find sum of number 1-5
'''def find_sum(n):
    if n==1:
        return n
    return n+find_sum(n-1)

if __name__=='__main__':
    print(find_sum(5))'''

#fibonacci-finds sum of previous 2 numbers
def fib(n):
    if n==0 or n==1:
        return n 
    return fib(n-1)+fib(n-2)

if __name__=='__main__':
    print(fib(6))