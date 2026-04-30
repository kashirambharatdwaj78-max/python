def vowels(a):
  count=0
  for b in a:
    if b=="a" or b=="e" or b=="i" or b=="o" or b=="u" or b=="A" or b=="E" or b=="I" or b=="O" or b=="U":
      count=count+1
    else:
      continue
  return count
s=vowels(str(input("enter details::")))
print(s)
    

  

