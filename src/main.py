#ent an text to get its reverse
def reverse(a):
  s=[]
  for c  in range(len(a)-1,-1,-1):
    #these range is used to add elements to the above list
    #in reverse
  
    s.append(a[c])
  p=""
  i=0
  while i<len(s):
    #these add character from reverse list in an varible
  
    p=p+s[i]
    i+=1
  return p
  
s=reverse(input("ent: "))  
print(s)
    

  


