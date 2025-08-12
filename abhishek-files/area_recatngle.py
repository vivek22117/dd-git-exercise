# Your code here
def calculate_rectangle_area(length,bredth):
  """function for calculating area of rectangle"""
  area= length*bredth
  return area
  

# --- Test Cases ---
area1 = calculate_rectangle_area(10, 5)
print(f"The area of a 10x5 rectangle is: {area1}")  # Expected: 50

area2 = calculate_rectangle_area(7.5, 3)
print(f"The area of a 7.5x3 rectangle is: {area2}") # Expected: 22.5

