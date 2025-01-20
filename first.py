import time

def fibboiter(n):
    prevNum = 0
    currentNum = 1
    for i in range(1,n):
         prevprevNum = prevNum
         prevNum = currentNum
         currentNum = prevNum + prevprevNum
    return currentNum
def fibborecur(n):
    if n==0:
        return 0
    elif (n==1):
        return 1
    else:
        fibborecur(n-1)+ fibborecur(n-2)

if __name__=="__main__":
        num=int(input("enter a number"));
        init = time.time()
        print(f"using recursion value of fib({num})is {fibborecur(num)}")
        print(f"using iter value of fib({num})is {fibboiter(num)}")
        print(f"it took {time.time()-init}seconds");