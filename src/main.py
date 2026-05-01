def r_duplicate(a):
  for c in a:
    a.remove(c)
    if c not in a:
      a.append(c) 
  print(a)
r_duplicate("hello")
      
      
    
  

