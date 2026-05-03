def force(a,b,c):
  return round((6.67*10**(-11))*a*b/c**2,2)
a=float(input("ent mass1:"))
b=float(input("ent mass2:"))
c=float(input("ent distance:"))
s=force(a,b,c)
print("force is",s,"N")
