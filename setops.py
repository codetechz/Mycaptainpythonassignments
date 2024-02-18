A=set()
B=set()

#User input for set A
print("Enter the number of elements in set A:")
n1=int(input())
print("Enter the elements for set A")
for i in range(0,n1):
  elmnt1=int(input())
  A.add(elmnt1)

#User input for set B
print("Enter the number of elements in set B:")
n2=int(input())
print("Enter the elements for set B")
for j in range(0,n2):
  elmnt2=int(input())
  B.add(elmnt2)

print("Set1=",A)
print("Set2=",B)

print("Union of A and B is:",A|B)
print("Intersection of A and B is:",A&B)
print("Difference of A and B is:",A-B)
print("Symmetric Difference of A and B is:",A^B)
