def TEST(a):
  s=list(a)
  e=s.pop(0)
  if len(s)!=0:
   return TEST(s)
  return e
print(TEST(input("ent ")))  