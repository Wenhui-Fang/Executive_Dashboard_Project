# monthly_sales.py

# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

# File path = sales-201710.csv

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import datetime as dt
import pandas as pd
import operator

#converting float to USD adapted from https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

#ALL Variables
top_sellers = []
total_monthly_sales = 0.0
individual_monthly_sales = 0.0
df = pd.read_csv("sales-201904.csv")
total_monthly_sales = df['sales price'].sum()

#Getting unique product name
products = df["product"].unique()

#converting datatype to list
unique_product_list = products.tolist()

# filering approach adapted from https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py#L77

for product_name in unique_product_list:
    matching_rows = df[df["product"] == product_name]
    individual_monthly_sales = matching_rows["sales price"].sum()
    top_sellers.append({"name": product_name, "monthly sales": individual_monthly_sales})

top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly sales"), reverse=True)


# print(top_sellers)

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: + {as_currency(total_monthly_sales)}")

print("Product               Sum of sales price")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

for p in top_sellers:
    print(p["name"] + "             " + as_currency(p["monthly sales"]))

print("-----------------------")
print("VISUALIZING THE DATA...")

# TODO: make a chart

# adapted from code posted to matplotlib Slack channel: https://georgetown-opim-py.slack.com/archives/CFZDKNKA4/p1549494877005200

bar_data = top_sellers

product_list = []
sales_list = []

for p in bar_data:
  product_list.append(p["name"])
  sales_list.append(as_currency(p["monthly sales"]))

product_list.reverse()
sales_list.reverse()

#displaying labels using a loop
#adapted from https://www.reddit.com/r/learnpython/comments/2y9zwq/adding_value_labels_on_bars_in_a_matplotlib_bar/

plt.barh(product_list,sales_list, align = "center")

plt.ylabel("Products")
plt.xlabel("Sales")

for a,b in zip(sales_list,product_list):
  plt.text(a, b, str(a))

plt.tight_layout()
plt.show()