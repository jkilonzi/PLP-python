def divisible_by_ten(num):
 result = num % 10
 if result == 0:
     return True
 else:
     return False
 
num = float(input("Enter a number: "))
 
result = divisible_by_ten(num)

print('Is',num,"divisible by 10?",result )
