def max_list(a):
  i=0
  s=len(a)-1
  while i<s:
    if a[0]<a[1]:
      a.remove(a[1])
      i=i+1
    elif a[1]<a[0]:
      a.remove(a[0])
      i=i+1
  return a[0]
    
s=max_list(list(map(int,input(' ent list').split(","))))
print(s)
