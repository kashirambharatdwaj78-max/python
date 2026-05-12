def ANA(a,b):
  u,i=sorted(list(a)),sorted(list(b))
  while u[0]==" ":
    u.pop(0)
  while i[0]==" ":
    i.pop(0)
  if u==i :
    return f"{a} AND {b} : THEY ARE ANAGRAM"
  else:
    return "THEY ARE NOT"
a=input("ent 1:")
b=input("ent 2:")
print(ANA(a,b))
