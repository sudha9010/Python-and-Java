def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def main():
    number = int(input("Enter a number: "))
    factorial = calculate_factorial(number)
    print(f"Factorial of {number} is: {factorial}")

if __name__ == "__main__":
    main()
