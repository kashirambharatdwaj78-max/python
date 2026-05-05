import random
def BULLS(a):
  b=0
  c=0
  d={}
  s=list(str(a))
  r=str(random.randint(10,99))
  e=list(r)
  if a==r:
    return 'you win your luck is insane'
  else:
    for k in range(2):
      if a[k]==r[k]:
        b+=1
        s[k]="$"
        e[k]="@"
    for i in range(2):
      if s[i] in e:
        c+=1
    d["bulls"]=b
    d["cows"]=c
    return d
s=BULLS(input("guess an no."))
print(s)
      
