list1 = [21,3,4,33,2,3,10,3,76]
even, odd = 0, 0

for num in list1:
   if num % 2 == 0:
      even += 1
   else:
      odd += 1
print("Even numbers : ", even)
print("Odd numbers : ", odd)