n=int(input())
arr=list(map(int,input().split()))
rem=arr[-1]%10
if rem==0:
        print("Yes")
else:
        print("No")