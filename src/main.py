def prime(a):
  p=[]
  if a==2:
    p.append(a)
  else:
    for c in range(2,a+1):
      for k in range(2,c):
        if c%k==0:
          break
        elif k==c-1:
          p.append(c)
  return p
s=prime(int(input("ent no.")))
print(s)
      
        
      
      
        
     
