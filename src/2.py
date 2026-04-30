def word_count(a):
  c=0
  word=0
  while c<len(a):
    if a[c]==" ":
      word=word+1
    c=c+1
  return word+1
s=word_count(str(input("ent profile detail:")))
if s>50:
  print('surpases word limit please enter again')
  s=word_count(str(input("ent profile detail:")))
  print(s)

print(s)

  


  

    



