# name = str(input("enter your name"))
# print(name,"how are you")
list = []
for i in range(1,4):
    num = int(input(f"enter your {i} favourite number:"))
    list.append(num)
print(list)
for num in list:
    if num % 2 == 0:
        print(f"the number {num} is even")
    else:
        print(f"the number {num} is odd")
tu = tuple(list)
for num in list:
    print("here is the number and its square",(num,num**2))
total = 0
for num in list:
    total += num
    print(f"here is the sum of your favourite numbers",total)
i = 2
if total <= 1:
    print(f"{total} is not a prime number")
    if total == 2:
        print(f"{total} is a prime number")
        for i in range(2,total):
            if total % i == 0:
                print(f"{total} is a prime number")
            else:
                print(f"{total} is not a prime number")
total = 10
is_prime(total)
# Define the is_prime function BEFORE calling it
def is_prime(n):
    if n <= 1:
        print(f"{n} is not a prime number")
        return False
    elif n == 2:
        print(f"{n} is a prime number")
        return True
    else:
        for i in range(2, int(n**0.5) + 1):  # Only check up to the square root of n for efficiency
            if n % i == 0:
                print(f"{n} is not a prime number")
                return False
        print(f"{n} is a prime number")
        return True

# Example input and process
total = 10  # Example value

# Call the is_prime function
is_prime(total)
numbers = []
for i in range(1, 4):
    num = int(input(f"Enter your {i} favourite number: "))
    numbers.append(num)

print("Your favourite numbers are:", numbers)
for num in numbers:
    if num % 2 == 0:
        print(f"The number {num} is even")
    else:
        print(f"The number {num} is odd")
num_tuple = tuple(numbers)
for num in numbers:
    print(f"Here is the number and its square: {num} and {num**2}")
total = 0
for num in numbers:
    total += num
    print(f"Here is the sum of your favourite numbers: {total}")
is_prime(total)

