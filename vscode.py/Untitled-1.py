print("the random number is between 1 and 50")
z=int(input("enter your guess:" ))
y=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,38,39,40,41,42,43,44,45,46,47,48,49,50]
for z in y:
  z=int(input("enter your guess:" ))
  print(z)
  if z==15:
    
    break
  elif z ==range(1,9+1):
    print("a bit too lower")
  elif z== range(10,14+1):
    print("clooose")
  elif z== range(16,20+1):
    print("clooose")
  elif z== range(21,50+1):
    print("a bit too high")
print ("u got it!")
