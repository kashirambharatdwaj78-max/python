def MIN(a):
  max=a[0]
  for k in a:
    if max<k:
      max=k
  return max
def S(a):
  a.remove(MIN(a))
  return MIN(a)
print(S(list(map(int,input("ENT ARRAY :").split(",")))))

  
 
