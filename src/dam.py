def CON(a):
  p={}
  s=[]
  t=[]
  for k in a:
    i=0  
    for d in a:
      if k==d:
        i+=1
        s.append(i)
    p[k]=i 
  for q in p:
    if p[q]==max(s):
      t.append(q)   
  print(f'''  
MOST USED WORD'S ARE
  
{t}''')
          
CON(input("ENT A PARAGRAPH : ").split())
