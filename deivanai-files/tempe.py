# Your code here
def celsius_to_fahrenheit(cel_temp):
    '''This function converts a temperature from Celsius to Fahrenheit. '''
    far_temp = cel_temp* 9/5 + 32
    return far_temp





# --- Test Cases ---
f_temp1 = celsius_to_fahrenheit(0)
print(f"0°C is {f_temp1}°F")  # Expected: 32.0

f_temp2 = celsius_to_fahrenheit(100)
print(f"100°C is {f_temp2}°F") # Expected: 212.0