Here’s a Python program based on the assignment that checks if numbers are even or odd, calculates their squares, sums the numbers, and checks if the sum is a prime number.

```python
# Import math library to check for prime numbers
import math

# Function to check if a number is prime
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# Function to determine if a number is even or odd
def even_or_odd(number):
    return "even" if number % 2 == 0 else "odd"

# Start of the program
def explore_numbers():
    # Get user's name
    name = input("Enter your name: ")

    # Get three favorite numbers from the user and store them in a list
    numbers = []
    for i in range(1, 4):
        num = int(input(f"Enter your {i} favorite number: "))
        numbers.append(num)

    # Greet the user
    print(f"\nHello, {name}! Let's explore your favorite numbers:")

    # Check if the numbers are even or odd and store the results in a list of tuples
    even_odd_info = [(num, even_or_odd(num)) for num in numbers]
    
    # Print whether each number is even or odd
    for num, eo in even_odd_info:
        print(f"The number {num} is {eo}.")

    # Calculate the square of each number and print them
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num**2})")

    # Calculate the sum of the numbers
    total_sum = sum(numbers)
    print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")

    # Check if the sum is a prime number
    if is_prime(total_sum):
        print(f"Wow, {total_sum} is a prime number!")
    else:
        print(f"{total_sum} is not a prime number.")

# Run the program
explore_numbers()
```

### How it works:
1. **Input**: The user enters their name and three favorite numbers.
2. **Even/Odd Check**: The program determines if each number is even or odd.
3. **Squares**: The program calculates and prints the square of each number.
4. **Sum Calculation**: The sum of the three numbers is calculated and printed.
5. **Prime Check**: The program checks if the sum is a prime number and notifies the user.

### Example Output:

```
Enter your name: Alex
Enter your first favorite number: 4
Enter your second favorite number: 6
Enter your third favorite number: 9

Hello, Alex! Let's explore your favorite numbers:
The number 4 is even.
The number 6 is even.
The number 9 is odd.
The number 4 and its square: (4, 16)
The number 6 and its square: (6, 36)
The number 9 and its square: (9, 81)

Amazing! The sum of your favorite numbers is: 19
Wow, 19 is a prime number!
```