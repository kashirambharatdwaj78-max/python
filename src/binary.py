def RAN(a):
  e=[]
  i=0
  while 2**i<a:
    e.append(2**i)
    i+=1
  k=a-e[len(e)-1]
  if k not in e:
    return [e[len(e)-1]]+RAN(k)
    # these one just create loop until the final one run due to which no error come
  else:
    return [e[len(e)-1],k]
#these above one generate an list of no.s which are in term of 2**power and make the given a of sumed up
def CON(a):
  i=0
  e=[]
  while 2**i!=max(a):
    e.append(2**i)
    i+=1
  e.append(max(a))
  for k in e:
    if k in a:
      e[e.index(k)]=1
    else:
      e[e.index(k)]=0   
  e.reverse()
  return  e    
# these one above just check wether the given  no. in list e or not and then give them 1 or 0 as binary
print(CON(RAN(int(input("ENT NO.")))))

