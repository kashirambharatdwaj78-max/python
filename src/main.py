
def armstrong(a):
  k=str(a)
  i=0
  for c in k:
    i+=int(c)**len(k)
  if a==i:
    return True
  else:
    return False
  
  
  

  

  
    
  
s=armstrong(int(input("ent no. : ")))
print(s)
  
    
  

  
  
  
  



    
      
    