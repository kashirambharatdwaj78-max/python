import random
s=int(input("ent 1 to generate an password : "))
actual= (
    'z', 'n', 'T', 'A', 'T', 'p', '4', 'Z', 'H', 'v', 'J', 'j', 'h', 'B', 'm', 'm', 
    '1', 'a', 'I', 'C', 'I', 'L', '1', '9', '7', 'Z', 'a', 'B', 'h', '9', 'x', '6', 
    '7', 'B', 'v', 'v', 'U', 'W', 'p', 's', 'F', '7', 'T', 'c', 'O', 'P', 'M', 'S', 
    '3', 'H', 'N', 'Z', 'z', 'V', 'E', 'm', 'c', 'h', 'T', 'V', '2', '2', 'l', 'A', 
    'e', '9', 'F', 'd', 'h', 'S', '4', 'g', 'r', 'f', 'l', 'Y', 'z', 'u', 'p', 'O', 
    'Q', 'O', 'S', 'F', 'U', 'm', 'f', 'S', 'C', '9', 'K', 'U', 'S', 'n', 'n', 'C', 
    'b', 'M', 'a', 'i'
)

if s==1:
  i=0
  k=[]
  while i<10:
    r=random.choice(actual)
    k.append(r)
    i+=1
e=""
for d in k:
  e=e+d


    
print(e)
