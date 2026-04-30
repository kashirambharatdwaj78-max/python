def r_duplicate(a):
  d=1
  for c in a:
    while d<len(a):
      if c!=a[d]:
        d=d+1
      else:
        a.remove(str(c))
    return a
s=r_duplicate(input('enter list of canditades:').split(","))
print(s)

      
    
  
    
  
    
  

  

