l1=[]
l2=[]
print("Enter the number of elements in the list:")
n=int(input())
print("Enter the elments of the list:")  
for i in range(0,n):
 elmnt=int(input())    
 l1.append(elmnt)
print("The input list is:",end=" ")
print(l1)
for elmnt in l1:
 if elmnt>=0:
  l2.append(elmnt)
print("The list of positive numbers is:",end=" ")
print(l2)
