#CountDown
def Countdown(positive_count):
  if positive_count < 0:
    print("please provide positive integer only")
  else:
    print(f"Starting {positive_count}-second countdown:")
    while positive_count>0:
      print(positive_count)
      positive_count-=1
    print("Blast off!")
Countdown(10)

