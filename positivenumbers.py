list=[]
print("Enter the length of the list:")
n=int(input())
for x in range(0,n):
 ele=int(input("Enter the elements of list:"))
 list.append(ele)
print("POsitive numbers in",list,"are:")
for x in list:
 if x>=0:
  print(x,end=" ")
  
