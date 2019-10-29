x=float (input("Введите первое число:"))
z=input ("Введите действие (+, -, /, *, //)")
y=float (input("Введите второе число:"))
if z=="+":
   res=x+y
elif z=="-":
   res=x-y
elif z=="*":      
   res=x*y 
if z=="/":
    res=x/y
elif z=="//":
    res=x//y
print ("Результат =", res)
