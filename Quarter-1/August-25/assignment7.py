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
def is_prime(n):
    if n <= 1:
        print(f"{n} is not a prime number")
        return False
    elif n == 2:
        print(f"{n} is a prime number")
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                print(f"{n} is not a prime number")
                return False
        print(f"{n} is a prime number")
        return True

total = 10
is_prime(total)

                
                