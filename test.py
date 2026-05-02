def grading(a):
  s=[]
  a.append(sum(a)/5)
  for c in a:
    if c>90:
      s.append("A")
    elif c>80:
      s.append("B")
    else:
      s.append("C")
  k=s[len(s)-1]
  s.remove(s[len(a)-1])
  return s,"TOTAL grades: ",k
s=grading(list(map(int,input("marks[math,physics,chemistry,optional,english]:    ").split(","))))
print(s)

  
  




