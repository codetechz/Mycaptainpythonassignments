f1=0
f2=1
sum=0
print("Enter the number of terms: ")
n=int(input())
for i in range(0,n):
 f1=f2
 f2=sum
 print(sum,",",end="")
 sum=f1+f2

