def fiboni(l):
  a=[0,1]
  while len(a)<l:
    a.append(a[len(a)-1]+a[len(a)-2])
  return a
s=fiboni(int(input("ent limiting value of series:")))


print(s)
  
    
  

  

  
