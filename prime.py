import math

# For checking if a number is Prime or not.
def is_prime(a):
    dec = 1
    if a == 1:
        print("Not Prime")
    elif a == 2:
        print("Prime")
    elif a > 2 and a % 2 == 0:
        print("Not Prime")
    else:
        max_div = math.floor(math.sqrt(a))
        for i in range(3, 1+max_div, 2):
            if a % i == 0:
                print("Not Prime")
                dec = 0
                break
        if dec == 1:
            print("Prime")
            
# For making a list of all prime number withing the range (1 to num)
# num is a number given by a user.
def ls_prime(b):
    prime_list = list()
    prime = [True for i in range(b+1)]
    p = 2
    while(p * p <= b):
        if (prime[p] == True):
            for i in range(p * p, b + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for p in range(2, b):
        if prime[p]:
            c += 1
            prime_list.append(p)
    print(prime_list)
    return c

print("1 Check if number is Prime or not?")
print("2 Generate a list of Prime number.")
choice = input("Enter your choice: ")

try:
    choice = int(choice)
    if choice ==1 or choice ==2:
        num = input("Enter the number: ")
        try:
            num = int(num)
        except:
            print("Enter a positive Integer!")
        if choice == 1:
            is_prime(num)
        elif choice == 2:
            c = ls_prime(num)
            print("Total prime numbers in range:", c)
    else:
        print("Wrong Choice!")
except:
    print("Enter Command Number!")
