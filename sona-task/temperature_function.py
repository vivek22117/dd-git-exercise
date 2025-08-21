#------Code here
def celsius_to_fahrenheit(celsius):
  f_temp =( celsius * (9/5)) + 32
  return(f_temp)


#-----Test Cases----------
f_temp1=celsius_to_fahrenheit(0)
print(f"0°C is {f_temp1}°F")

f_temp2=celsius_to_fahrenheit(100)
print(f"100°C is {f_temp2}°F")



