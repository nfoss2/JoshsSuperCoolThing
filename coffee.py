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
    print("The {} beverage you should order today is a {} {}".format(temperature, random.choices(syrups, weights=syrupsProbs), random.choices(hotCoffeeType, weights=hotCoffeeProbs)))
  elif temperature == "cold":
    print("The {} beverage you should order today is a {} {}".format(temperature, random.choices(syrups, weights=syrupsProbs), random.choices(coldCoffeeType, weights=coldCoffeeProbs)))
  else:
    user_input = input("Whoops didn't recognize that, please try again (hot/cold) ")
    generateCoffee(user_input)
     



def rescaleProbs():
    with open("./orderProb.json", "r") as json_file:
      coffee = json.load(json_file)
    
  # Extract syrups dictionary from data
    sProbs = coffee.get("syrups", {}) 
    # Calculate the sum of all syrup weights
    total_weight = sum(sProbs.values())
    # Normalize the syrup weights to sum up to 1
    normalized_syrups = {syrup: weight / total_weight for syrup, weight in sProbs.items()}
    # Update the data with normalized syrup weights
    sProbs["syrups"] = normalized_syrups
    
  # Extract syrups dictionary from data
    hProbs = coffee.get("hotCoffeeType", {}) 
    # Calculate the sum of all syrup weights
    total_weight = sum(hProbs.values())
    # Normalize the syrup weights to sum up to 1
    normalized_syrups = {syrup: weight / total_weight for syrup, weight in hProbs.items()}
    # Update the data with normalized syrup weights
    hProbs["hotCoffeeType"] = normalized_syrups
    
    with open("./orderProb.json", "w") as json_file:
      json.dump(coffee, json_file, indent=2)


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
    rescaleProbs()
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
