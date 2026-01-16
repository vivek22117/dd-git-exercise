import time

def process_data(data):
  try:
    start_time=time.time()
    print("Start processing data")
    if not isinstance(data, list):
      raise TypeError("Input data must be a list.")
    
    if len(data) > 100:
      raise ValueError("Data list is too long.")
    
    for i, value in enumerate(data):
      if not isinstance(value, (int, float)):
        raise TypeError(f"Element at index {i} is not a number : {value}")
      #Simulate processing
      time.sleep(3)
      result = sum(data)
      print("Result of processing : ", result)
      return result
  except TypeError as e:
    print(f"TypeError : {e}")
    return None 
  except ValueError as e:
    print(f"ValueError : {e}")
    return None  
  except Exception as e:
    print(f"TAn unexpected error occured: {e}")
    return None 
  finally:
    end_time = time.time()
    print(f"Processing time: {end_time - start_time: 2f} seconds")

#valid data
my_data=[1,2,3,4,5]
process_data(my_data)    

#invalid data 
my_data="print"
process_data(my_data)  

# data with non-numeric element
my_data=[1,2,"a",4,5]
process_data(my_data) 

#long data
my_data=list(range(103))
process_data(my_data)  
