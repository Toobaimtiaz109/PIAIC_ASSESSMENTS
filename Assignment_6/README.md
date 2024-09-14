# Python Code: Favorite number Analysis
---
[For more...](https://github.com/JahanzaibTayyab/Batch-62/blob/main/python-learning/assignments/Number_Exploration_Tool.md)

This script prompts the user to input their name and their three favorite numbers. It then performs several operations and outputs the results, including determining whether the numbers are even or odd, calculating the square of each number, and checking if the sum of the numbers is a prime number.

## 1. Initialization
Initialize the list to store the favorite number.
```python 
# Initialization
num_list:list = []
```
## 2. Collecting User Input
Ask the user to enter their name and then ask them for three of their favorite numbers. 
```python
# Prompt the user to enter their name
name:str = input("Enter your name here: ")

# Prompt the user to enter Favorite numbers and then store it in a list
for i in range(1,4):
    num:int = int(input(f"Write your {i} favorite number: "))
    num_list.append(num)
```
## 3. Greeting the user
The script greets the user by name and starts exploring their favorite numbers.
```python 
# Greeting user a message
print(f"\nHello {name}, lets explore your favorite numbers: ")
```
## 4.Even or Odd Check
This script check that whether the numbers are even or odd and then store this in a separate tuple.
```python
for item in num_list:
    if item % 2 == 0:
       print(f"The number {item} is the even number. ")
    else:
       print(f"The number {item} is the odd number. ")
```

## 5. Calculating Squares
The script calculates the square of each number in num_list.
It prints each number along with its square.
```python
# Calculate the square of the numbers provided by the user
for item in num_list:
    print(f"The number {item} and its square:({item} , {item ** 2})")
```
## 6. Sum Calculation
The script calculates the sum of the numbers in num_list.
It prints the sum of the favorite numbers.
```python
# Sum the numbers and store it in a separate variable
sum_of_num:int = sum(num_list)
print(f"Amazing! The sum of your favorite numbers is: {sum_of_num}")
```
## 7. Prime Number Check

The script checks if the sum of the favorite numbers is a prime number.
It uses a basic algorithm to determine whether the sum is prime or not.
```python
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
```

