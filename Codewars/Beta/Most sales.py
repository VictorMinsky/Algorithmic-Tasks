"""
You work in the best consumer electronics corporation and your boss wants to find out what three products generate the most sales. His 3 lists always look like this with various lenghts.

product["Computer", "Cell Phones", "Vacuum Cleaner"]

amount[3,24,8]

price[199,299,399]

given those three numbers, please return the three product names with the most sales (amount*price).

Solution: ["Cell Phones", "Vacuum Cleaner", "Computer"]

If two sales equal each other, return the first product name of the list.
"""



def top3(product, amount, price):
    return [i[0] for i in sorted(list(zip(product, amount, price)), reverse=True, key=lambda x: x[1] * x[2])[:3]]