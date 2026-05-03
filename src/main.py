def prime(k):
  if k==2:
    return True
  else:
    for o in range(2,k):
      if k%o==0:
        return False
    return True
def prime_factor(a):
  p=[]
  q=[]
  power=[]
  for c in range (2,a):
    if a%c==0:
      p.append(c)
  for d in p:
    if prime(d) is True:
      q.append(d)
  for u  in q:
    i=1
    while a%u**i==0:
      i+=1
    power.append(i-1)
  return q,power       
s=prime_factor(int(input("ent no: ")))
i=0
while i<len(s[0]):
  print(s[0][i],"to the power",s[1][i])
  i=i+1



      
        
      
      
        
     
