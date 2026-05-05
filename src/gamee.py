import random
def Game(a):
  r=random.choices(("rock","paper","scissors"))
  i=r[0]
  
  if a=="rock":
    if i==a:
      return (a,"vs",i),("results : ","draw")
    elif i=="paper":
      return (a,"vs",i),("results : ","lose")
     
    elif i=="scissors":
      return (a,"vs",i),("results : ","win")
  if a=="paper":
    if i==a:
      return (a,"vs",i),("results : ","draw")
    elif i=="scissors":
      return (a,"vs",i),("results : ","lose")
     
    elif i=="rock":
      return (a,"vs",i),("results : ","win")
  if a=="scissors":
    if i==a:
      return (a,"vs",i),("results : ","draw")
    elif i=="rock":
      return (a,"vs",i),("results : ","lose")
     
    elif i=="paper":
      return (a,"vs",i),("results : ","win")
  s=Game(input('ent "rock","paper",scissors : '))
  print(s)
  i=int(input("ent 0 to end:"))
    
    
