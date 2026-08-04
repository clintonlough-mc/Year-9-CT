"""
Year 9 Python Challenge 1

Instructions:
 - Read the tasks below.
 - Add code where the TODO comments are.
 - Use print(), input(), assign variables, and perform simple math operations.
 - Keep your code neat and add comments if you want using the # symbol.

Tasks:
1) Print a welcome message that asks for the users name and says hello to them.

2) Create two variables: an integer called 'apples' and another integer called 'oranges'.
	Assign them any small whole-number values you like.

3) Show the user what fruits are available and their prices in cents. Ask the user how many of each fruit they want to buy.

4) Imagine each apple costs 30 cents and each orange costs 50 cents.
	Calculate the total cost in cents and store it in 'total_cost_cents'.
	Then calculate the cost in dollars as a floating-point number in 'total_cost_dollars'.
	Print both values using clear messages.

5) Bonus (optional): Keep track of how many fruits the user has bought and update it each time they buy more.

Starter code: add your answers where the TODO markers are.
"""

# ======= START OF STUDENT CODE AREA =======

# Welcome message: ask for the user's name and introduce the fruit store
user_name = input("Welcome! What's your name? ")
print(f"Hello, {user_name}! Welcome to the Python Fruits Store.")

# Fruit options and prices (in cents)
apple_cost_cents = 30
orange_cost_cents = 50
print("We have the following fruits for sale:")
print(f"1) Apples - {apple_cost_cents} cents each")
print(f"2) Oranges - {orange_cost_cents} cents each")

# Ask the user how many of each fruit they want to buy
try:
	apples = int(input("How many apples would you like to buy? "))
except ValueError:
	apples = 0
try:
	oranges = int(input("How many oranges would you like to buy? "))
except ValueError:
	oranges = 0

# Calculate totals and show the price
total_fruits = apples + oranges
total_cost_cents = apples * apple_cost_cents + oranges * orange_cost_cents
total_cost_dollars = total_cost_cents / 100.0
print(f"You are buying {total_fruits} fruits in total.")
print(f"Total cost: {total_cost_cents} cents")
print(f"Total cost: ${total_cost_dollars:.2f}")

# Bonus behaviour: offer a simple discount if the customer buys more than 10 items
if total_fruits > 10:
	discount_cents = int(total_cost_cents * 0.10)
	discounted = (total_cost_cents - discount_cents) / 100.0
	print(f"You get a 10% discount! New total: ${discounted:.2f}")

# ======== END OF STUDENT CODE AREA =======

if __name__ == "__main__":
	 # Student code runs on import because it's at top-level. Nothing further required.
	 pass
