
import random
i=0
o=0
game=""
while game!="q":
  r=random.randint(1,10)
  g=input("ent q to quit,guess an no. : ")
  if g=="q":
    
  
    game=g
    print("points earner: ",i,"no. of trials",o)
  else:
    o+=1
  
    if int(g)==r:
      print("correct")
    
      i+=10
  
    else:
      print("false")