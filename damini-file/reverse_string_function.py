

def brute_force_reverse(a):
  b=""
  for i in range(len(a)-1, -1, -1 ):
    # print(a[i])
    b+=a[i]
  return b 

reversed1=brute_force_reverse("hello")
print(f"'engineer' reversed is '{reversed1}'")

reversed2=brute_force_reverse("engineer")
print(f"'engineer' reversed is '{reversed2}'")





# for i in a:
#   print(i)
#   b+=i
