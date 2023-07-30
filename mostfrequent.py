W=input("Input a string:")
def make_dict(string):
 d=dict()
 for key in string:
  if key not in d:
   d[key]=1
  else:
   d[key]+=1
 return d
print( make_dict(W))

def most_frequent(W):
    letters = [letter.lower() for letter in W if letter.isalpha()]
    dictionary = make_dict(letters)
    result = []
    for key in dictionary:
        result.append((dictionary[key], key))
    result.sort(reverse=True)
    for count, letter in result:
        print (letter, count)

most_frequent(W)


