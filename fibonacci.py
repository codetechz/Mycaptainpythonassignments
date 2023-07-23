print("Enter number of terms to be printed for Fibonacci Series:")
n=int(input())
f0=0
f1=1
temp=0
count=1
while count<=n:
 print(temp,end=" ")
 f0=f1
 f1=temp
 temp=f0+f1
 count+=1
