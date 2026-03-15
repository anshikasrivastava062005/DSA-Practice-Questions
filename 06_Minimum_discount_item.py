'''
Mayuri buys “N” no of products from a shop. The shop offers a different percentage of discount on
each item. She wants to know the item that has the minimum discount offer, so that she can avoid
buying that and save money.
[Input Format: The first input refers to the no of items; the second input is the item name, price and
discount percentage separated by comma (,) ] Assume the minimum discount offer is in the form of
Integer.
Note: There can be more than one product with a minimum discount.
Sample Input 1:
4
mobile,10000,20
shoe,5000,10
watch,6000,15
laptop,35000,5
Sample Output 1:
shoe
Explanation: The discount on the mobile is 2000, the discount on the shoe is 500, the discount on the
watch is 900 and the discount on the laptop is 1750. So the discount on the shoe is the minimum.'''

n = int(input())  # number of items

items = []
discounts = []

for _ in range(n):
    name, price, percent = input().split(",")
    
    price = int(price)
    percent = int(percent)
    
    discount_amount = (price * percent) // 100
    
    items.append(name)
    discounts.append(discount_amount)

min_discount = min(discounts)

for i in range(n):
    if discounts[i] == min_discount:
        print(items[i])