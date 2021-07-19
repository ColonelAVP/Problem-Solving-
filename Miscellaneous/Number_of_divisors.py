# Fn to find number of divisors including excluding number and 1
def divisors(num1):
    all_numbers = []
    for i in range(2, num1):
        if num1 % i == 0:
            all_numbers.append(i)
    return f"The number of divisors of given number are {len(all_numbers)}"


# Driver's Code
num1 = int(input("Enter a Integer: "))
print(divisors(num1))
