def CON(a):
  if a==1:
    return "1"
  return CON(a//2)+str(a%2)
print(CON(int(input("ENT NO."))))
  
  
