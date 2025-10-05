# 1. dice roller
import random
def roll_dice(): 
    return random.randint(1, 6)
def main():
    print("Welcome to the Dice Roller!")
  while True:
        input("Press Enter to roll the dice...")
        dice_result = roll_dice()
        print(f"You rolled a {dice_result}!")
        
        # if user wants to roll the dice again
        again = input("Do you want to roll again? (yes/no): ").lower()
        if again != 'yes':
            print("Thank you for playing!")
            break
if __name__ == "__main__":
    main()


# 2. To check whether a number is even or odd
a= int(input("enter a number:"))
if (a%2==0):
  print("Number is even")
else:
  print("Number is odd")


# 3. largest number
def largest_number():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    if a >= b and a >= c:
        print("The largest number is a")
    elif b >= a and b >= c:
        print("The largest number is b")
    else:
        print("The largest number is c")

if __name__ == "__main__":
    largest_number()


# 4. temperature converter
def celsius_to_fahrenheit():
    temp = float(input("Enter temperature in Celsius: "))
    fahrenheit = (temp * 9/5) + 32
    print(fahrenheit)

if __name__ == "__main__":
    celsius_to_fahrenheit()
