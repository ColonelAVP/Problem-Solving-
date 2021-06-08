# Problem to convert temperature from celcius to fahrenheit or vice-versa

print("Use F for fahrenheit, C for Celcius")
temp = input("Enter Temp in celsius/fahrenheit:")
value = int(temp[:-1])
metrics = temp[-1].upper()
print(f"The temperature is {value} {metrics}")
if metrics == 'C':
    print("The Temperature in fahrenheit is: ",(value*9/5)+32,"F")
elif metrics == "F":
    print("The temperature in Celcius is: ",(value-32)*5/9,"C")
else:
    raise ValueError








