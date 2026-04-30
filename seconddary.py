def fiboni(l):
  a=[0,1]
  while a[len(a)-1]<l:
    a.append(a[len(a)-1]+a[len(a)-2])
  q=l
  if a[len(a)-1]>l:
    a.remove(a[len(a)-1])
  return a
s=fiboni(int(input("ent limiting value of series")))


print(s)
  
    
  

  

  
