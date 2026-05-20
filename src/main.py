def REM(a):
  d={}
  a=list(a)
  for k in a:
    i=a.count(k)
    d[k]=i-1
  for s in d:
    if s==" ":
      continue   
    else:
      for k in range(d[s]):
        a.remove(s)  
  a="".join(a)
  return a
print(REM(input("ent text :")))
    
      
    
      
    
  

    
      
    
  