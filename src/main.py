def reverse(a):
  s=[]
  for c  in range(len(a)-1,-1,-1):
    s.append(a[c])
  p=""
  i=0
  while i<len(s):
    p=p+s[i]
    i+=1
  return p
  
s=reverse(input("ent: "))  
print(s)
    

  


