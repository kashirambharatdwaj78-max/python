def r_duplicate(a):
  s=a  
  for c in a:
    i=0
    for d in a:
      if c==d:
        i+=1
    for k in range(i-1):
      s.remove(c)  
  return s       
s=r_duplicate(input('ent list:  ').split(","))
print(s)
      
    
    
  





