# Refer to the README.md file in this project for a description 
# of the challenge and requirements. When viewing the README.md, 
# replit will show an option to Open Preview, which will open a 
# more readable view.

# The Python module math is imported and available to use but not required.
# Please do not import any additional modules (such as NumPy).
import math

tea_bases = {
  "milk" : 4.35,
  "oolong" : 4.60,
  "rose" : 5.85,
  "mango" : 5.47,
}
topping_add_ons = {
  "boba" : 0.50,
  "lychee" : 0.75,
  "jelly" : 0.65,
  "taro" : 1.00,
  "chia" : 0.35
}
loyalty_discount = False

def bubble_tea_calculator(tea_base, add_ons, loyalty_discount):
    # Place your implementation for bubble_tea_calculator here, 
  total = 0
  total += tea_bases.get(tea_base)
  for i in range(len(add_ons)):
    total += topping_add_ons.get(add_ons[i])
  if loyalty_discount == True:
    # $1.00 discount
    # total -= 1.00
    # 15% discount
    discount_total = total * .15
    total -= discount_total
  # original print result did not show second decimal if zero so needed a different way to format the print statement
  # print(f"The cost is ${str(round(total, 2))}")
  # print("The cost is ${:.2f}".format(total))
    
  # format string to show cost of tea base and topping add ons
  string_add_ons = " & ".join(add_ons)
  print(f"The cost of {tea_base} tea with {string_add_ons} is ${total:.2f}")
  return total

# You may call bubble_tea_calculator with your own arguments here.
# For example, if the following line is uncommented, and the Run button
# is clicked, it will call bubble_tea_calculator with the listed
# parameters. The supplied example uses the same arguments as the
# test Challenge01.
  
bubble_tea_calculator("milk", ["boba", "jelly", "taro"], False)
bubble_tea_calculator("rose", ["chia"], False)
bubble_tea_calculator("mango", [], True)

# The challenges are provided as a set of tests that can be run 
# from the Tests panel at the left (the icon looks like a check 
# mark). Clicking the Run tests button will run the Challenge 
# inputs against your code, displaying either a success message, 
# or a message about what was expected and what was observed.