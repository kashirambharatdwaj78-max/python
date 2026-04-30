def leap_year(year):
  if year%400==0:
    return "its an leap year"
  
  elif year%4==0 and year%100!=0:
      return "its an leap year"
  else:
    return 'not an leap year'   
y=int(input("year"))
s=leap_year(y)
print(s)




