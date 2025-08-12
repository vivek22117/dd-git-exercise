# Your code here
def celsius_to_fahrenheit(c_temp):
  """convert celcius into feranite"""
  f_temp = c_temp * 9/5 + 32
  return f_temp

# --- Test Cases ---
f_temp1 = celsius_to_fahrenheit(0)
print(f"0°C is {f_temp1}°F")  # Expected: 32.0

f_temp2 = celsius_to_fahrenheit(100)
print(f"100°C is {f_temp2}°F") # Expected: 212.0

f_temp3 = celsius_to_fahrenheit(35)
print(f_temp3)
