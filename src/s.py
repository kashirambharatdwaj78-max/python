def PRIME(a):
  e=[]
  for k in range(2,a+1):
    i=0
    for s in range (1,k):
      if k%s==0:
        i+=1
    if i==1:
      e.append(k)
  return e
def PRIME_FACTORS(a):
  d={}
  w=PRIME(a)
  if a in w:
    d[f"{a}^"]=1
    return d
  else: 
   for o in w:
     i=1
     while a%(o**i)==0:
       i+=1
     if i>1:
       d[f"{o}^"]=i-1
  return d
s=PRIME_FACTORS(int(input("ent no.")))
print(s)
    
      
    
      
    
    
  

    
      
    
      
    
  



  

