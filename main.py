MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient_resources(ingredient_requirements):
  """Returns True when order can be made, False if ingredients are insufficient."""
  sufficient_water = ingredient_requirements["water"] <= resources["water"]
  sufficient_coffee = ingredient_requirements["coffee"] <= resources["coffee"]

  if user_choice != "espresso":
      sufficient_milk = ingredient_requirements["milk"] <= resources["milk"]
      if sufficient_water and sufficient_coffee and sufficient_milk:
          return True
  else:
      if sufficient_water and sufficient_coffee:
          return True

  if not sufficient_water:
      print("Sorry, there is not enough ​water​.")
  elif not sufficient_coffee:
      print("Sorry, there is not enough ​coffee​.")
  elif user_choice != "espresso" and not sufficient_milk:
      print("Sorry, there is not enough ​milk​.")

  return False


def process_coins():
  """Returns the total calculated from coins inserted."""
  print("Please insert coins.")
  total = int(input("how many quarters?: ")) * 0.25
  total += int(input("how many dimes?: ")) * 0.1
  total += int(input("how many nickles?: ")) * 0.05
  total += int(input("how many pennies?: ")) * 0.01
  return total


def is_successful_transaction(coins, cost):
  """Return True when the payment is accepted, or False if money is insufficient."""
  if coins >= cost:
    global profit
    profit += cost
    return True
  
  else:
    print("Sorry that's not enough money. Money refunded.") 
    return False

def calculate_change(coins, cost):
  change = round(coins - cost, 2)
  print(f"Here is ${change} in change.")


def make_coffee(ingredient_requirements):
  """Deduct the required ingredients from the resources."""
  water = ingredient_requirements["water"]
  coffee = ingredient_requirements["coffee"]
  
  if user_choice != "espresso":
    milk = ingredient_requirements["milk"]
    resources["water"] -= water
    resources["coffee"] -= coffee
    resources["milk"] -= milk
    
  else:
    resources["water"] -= water
    resources["coffee"] -= coffee
  
  print(f"Here is your {user_choice} ☕ Enjoy!")


is_on = True

while is_on:
  user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
  
  if user_choice == "off":
    is_on = False
    
  elif user_choice == "report":
    print(f"""
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${format(profit, '.2f')}""")
  
  else:
    ingredient_requirements = MENU[user_choice]["ingredients"]

    if is_sufficient_resources(ingredient_requirements):
      cost = MENU[user_choice]["cost"]
      coins = process_coins()
      
      if is_successful_transaction(coins, cost):
        calculate_change(coins, cost)
        make_coffee(ingredient_requirements)
