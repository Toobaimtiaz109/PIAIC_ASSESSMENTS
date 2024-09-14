num_list:list = []
name:str = input("Enter your name here: ")
for i in range(1,4):
    num:int = int(input(f"Write your {i} favorite number: "))
    num_list.append(num)

print(f"\nHello {name}, lets explore your favorite numbers: ")
for item in num_list:
    if item % 2 == 0:
       print(f"The number {item} is the even number. ")
    else:
       print(f"The number {item} is the odd number. ")

for item in num_list:
    print(f"The number {item} and its square:({item} , {item ** 2})")

sum_of_num:int = sum(num_list)
print(f"Amazing! The sum of your favorite numbers is: {sum_of_num}")

is_prime = True
if sum_of_num <= 1:
    is_prime = False
for i in range(2,sum_of_num):
    if sum_of_num % i == 0:
        is_prime = False

if is_prime :
    print(f"Wow, The number {sum_of_num} is a prime number.")
else:
    print(f"Great Job, The number {sum_of_num} is not a prime number.")    


