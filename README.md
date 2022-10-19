# Ada's Bubble Tea Stand 

Click the Open Preview button above for a more readable view of these instructions.

>Candidates receiving this challenge may elect to work through live coding a solution during their interview time, or may choose to solve the challenge ahead of time and walk through their solution during the interview. Candidates who prefer to live code are strongly encouraged to review the challenge ahead of time, and are free to use any prepared notes during the interview. Candidates who prefer to fully develop a solution ahead of time should be ready to discuss and potentially make changes to their solution with their interviewer.

## Getting Started

Begin the challenge by opening the `main.py` file in the Files view on the left. If the Files view is not already visible, click the top icon in the column of icons on the left, which resembles a sheet of paper with a bent corner.

Do not modify any file other than `main.py`.

## Requirements
- You will write a function with the input and outputs specified below.
- Your function must use at least one loop or iterator.
- Your function must use at least one conditional statement.
- Your function must use at least one Dictionary or List to store data. You should be familiar with the features of _**both**_ data types, even if you only use one in your function.
- The Python module math is imported and available to use but not required. Please do not import any additional modules (such as NumPy). 

## Problem Statement
Bubble tea (also known as boba) is a Taiwanese drink consisting of a tea base and many different toppings such as chewy tapioca pearls or slurpable grass jelly. Ada aims to run the trendiest bubble tea spot in the neighborhood. The shop boasts reliable WiFi, an extensive drinks menu, and a great loyalty program. With your help, Ada’s Bubble Tea Stand will have the speediest order cost calculator in the industry.

- An order has one and only one base tea. The options are milk, oolong, rose, and mango. Their respective prices are listed below. 
- An order has between none and multiple add ons. The options are boba, lychee, jelly, taro, and chia. Their respective prices are listed below. 
- If a customer is part of the Ada Bubble Tea Stand loyalty program, _subtract $1.00_ from the order total. 
- The function called `bubble_tea_calculator` accepts three parameters:
  - `tea_base`, a string to represent the base tea in the bubble tea order. 
  - `add_ons`, a list of strings where each string represents the optional add ons to the order
  - `loyalty_discount`, a boolean that represents if the order was made by a customer in the loyalty program
- The function must print the price of the order in dollars (i.e., with two decimal places). Refer to the example output for the specific formatting.

### Tea Base
|Name|Price ($)|
|----|---------|
| milk | 4.35 |
| oolong | 4.60 |
| rose | 5.85 |
| mango | 5.47 |

### Add Ons
|Name|Price ($)|
|----|---------|
| boba | 0.50 |
| lychee | 0.75 |
| jelly | 0.65 |
| taro | 1.00 |
| chia | 0.35 |

## Examples

These examples are also provided as a set of tests that can be run from the Tests panel at the left (the icon looks like a check mark). Clicking the Run tests button will run the Challenge inputs against your code, displaying either a success message, or a message about what was expected and what was observed.

### Example 1
#### Input (arguments of the function)
```
tea_base = "milk"
add_ons = ["boba", "jelly", "taro"]
loyalty_discount = False
```
#### Output (printed by the function)
```
The cost is $6.50
```

### Example 2
#### Input (arguments of the function)
```
tea_base = "rose"
add_ons = []
loyalty_discount = False
```
#### Output (printed by the function)
```
The cost is $5.85
```

### Example 3
#### Input (arguments of the function)
```
tea_base = "oolong"
add_ons = ["chia"]
loyalty_discount = True
```
#### Output (printed by the function)
```
The cost is $3.95
```
