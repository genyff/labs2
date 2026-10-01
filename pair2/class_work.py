#ітерація - виконання одного циклу
#for i in range(5):
 #   i = i + 1
  #  print(i) #i += 1
#інкремент - операцiя збiльшення на одиницю
#for i in range(1, 6):
 #   print(i)

#i = 1
#while i <=5:
   # print(i)
   # i+=1

  # suma = 0

#n = int(input())#10
#for i in range(1, n + 1):
   # suma += i
#print(suma)

#f = 1

#n = int(input())  # 10
#for i in range(1, n + 1):
  #  f *= i
#print(f)

#n=int(input())
#count=0
#for i in range(1,n+1):
   # if i % 2 == 0:
      #  count +=1
       # print(count)
#game = True
#while True:
   # n=int(input("введи число , для виходу введи - 0 "))
    #if n==0:
       # game = False
     #   print(n)
#while True:
  # n=int(input("введи число , для виходу введи - 0 "))
    #if n==0:
   #    break
     #   print(n)

#for i in range(1, 11)
   # if i % 2 == 0
     #   continue
     #   print(i)

#n = 5012434
#suma = 0
#while n>0:
 #   digit = n % 10
  #  suma =+ digit
   # n = n//10
#print(suma)

#n = 123452
#max_digit = 0
#while n>0:
 #   digit = n % 10
  #  if digit > max_digit:
   #     max_digit = digit
#for i in range(1, 4):
 #   for j in range(1, 4):
  #      print(i, j)
  for row in range(hight):
      for col in range(width):
          print("*",end=" ")
          print()