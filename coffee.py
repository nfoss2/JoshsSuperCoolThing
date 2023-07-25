"""
Authors: Austin and Natalie
Purpose: Happy birthday Josh! 
"""
import random
import argparse
import json

print("Josh's Coffee Application!")

syrups = ["hazelnut", "lavender", "vanilla", "caramel"]
hotCoffeeType = ["latte", "americano", "cappuccino", "black coffee"]
coldCoffeeType = ["iced Latte", "iced americano", "cold brew", "iced coffee"]

def generateCoffee(temperature):
  with open("./orderProb.json", "r") as json_file:
    coffee = json.load(json_file)
   
  # Get the probability of choosing particular drinks 
  syrupsProbs = [coffee["syrups"]["hazelnut"], coffee["syrups"]["lavender"],
                coffee["syrups"]["vanilla"], coffee["syrups"]["caramel"]]
  hotCoffeeProbs = [coffee["hotCoffeeType"]["latte"], coffee["hotCoffeeType"]["americano"],
                    coffee["hotCoffeeType"]["cappuccino"], coffee["hotCoffeeType"]["black coffee"]]
  coldCoffeeProbs = [coffee["coldCoffeeType"]["iced latte"], coffee["coldCoffeeType"]["iced americano"],
                    coffee["coldCoffeeType"]["cold brew"], coffee["coldCoffeeType"]["iced coffee"]]
    
  if temperature == "hot":
    print("The {} beverage you should order today is a {} {}".format(temperature, random.choices(syrups, weights=syrupsProbs)[0], random.choices(hotCoffeeType, weights=hotCoffeeProbs)[0]))
  elif temperature == "cold":
    print("The {} beverage you should order today is a {} {}".format(temperature, random.choices(syrups, weights=syrupsProbs)[0], random.choices(coldCoffeeType, weights=coldCoffeeProbs)[0]))
  else:
    user_input = input("Whoops didn't recognize that, please try again (hot/cold) ")
    generateCoffee(user_input)

def rescaleProbs(syrup : str, coffeeType : str) -> None:
  # Open the order probability
  with open("./orderProb.json", "r") as json_file:
    coffee = json.load(json_file)
    
    # finding the favorite syrup
    for key in coffee["syrups"].keys():
      if compare(key, syrup):
        coffee["syrups"][key] += 0.20
        break
    else:
      # Get new user input if mispelled and run again
      user_input = input("Whoops, that name isn't in our database. Make sure you've spelled it correctly and try again: ")
      newSyrup, newCoffee = splitString(user_input)
      rescaleProbs(newSyrup, newCoffee)

    # Checking if it is a hot coffee
    for key in coffee["hotCoffeeType"].keys(): 
      if compare(key, coffeeType):
        coffee["hotCoffeeType"][key] += 0.20
        break
    else:
      # Checking if it is a cold coffee
      for key in coffee["coldCoffeeType"].keys(): 
        if compare(key, coffeeType):
          coffee["coldCoffeeType"][key] += 0.20
          break
      else:
        # Get new user input if mispelled and run again
        user_input = input("Whoops, that name isn't in our drink list. Make sure you've spelled it correctly and try again: ")
        newSyrup, newCoffee = splitString(user_input)
        rescaleProbs(newSyrup, newCoffee)

    ## rescale the probs to equal 1
    for key in coffee.keys():
    # Extract syrups dictionary from data
      probs = coffee.get(key, {}) 
      # Calculate the sum of all syrup weights
      total_weight = sum(probs.values())
      # Normalize the syrup weights to sum up to 1
      normalized_syrups = {syrup: round(weight / total_weight, ndigits=3) for syrup, weight in probs.items()}
      # Update the data with normalized syrup weights
      coffee[key] = normalized_syrups
    
    with open("./orderProb.json", "w") as json_file:
      json.dump(coffee, json_file, indent=2)

def compare(first : str, second : str):
  """
  Little helper function to compare strings.
  
  args:
      first (str): first string.
      second (str): second string.
  """
  
  return first.replace(" ", "").lower() == second.replace(" ", "").lower()

def splitString(text):
  """Function to split a string with syrup and coffee type into separate strings

  Args:
      text (string): user input string with syrup first and coffee type next

  Returns:
      syrup, coffee
  """
  try:
    idx = text.index(" ")
    return text[:idx], text[idx+1:]
  except:
    user_input = input("{} is an invalid entry, please use form '<syrup> <coffee>'. Try again: ".format(text))
    return splitString(user_input)

def main():
  
    # Create an ArgumentParser object
  parser = argparse.ArgumentParser(description="A simple script to perform addition and subtraction.")

  # Add positional arguments
  parser.add_argument("-hot", help="Generate a hot coffee order",
                      action = "store_true",
                      required = False)
  parser.add_argument("-cold", help="Generate a cold coffee order",
                      action = "store_true",
                      required = False)
  parser.add_argument("--favorite", help="Pass the string of a coffee order you  \
                      enjoyed to increase the odds of getting that order again",
                      required = False)
  
  # Parse the command-line arguments
  args = parser.parse_args()
  
  if args.hot:
    while True:
      generateCoffee("hot")
      user_input = input("Would you like a different order (yes/no) ")
      if user_input.lower() == "no":
        return
                        
  elif args.cold:
    while True:
      generateCoffee("cold")
      user_input = input("Would you like a different order (yes/no) ")
      if user_input.lower() == "no":
        return
    
  elif args.favorite:
    syrup, coffee = splitString(args.favorite)
    rescaleProbs(syrup, coffee)
    return
  else:
    while True:
      # Welcome Josh to his application 
      user_input = input("Would you like a hot or cold coffee? ")
      temperature = user_input.lower()
      generateCoffee(temperature)
      
      user_input = input("Would you like a different order (yes/no) ")
      if user_input.lower() == "yes":
        generateCoffee(temperature)
      elif user_input.lower() == "no":
        return
      
if __name__ == "__main__":
  main()
