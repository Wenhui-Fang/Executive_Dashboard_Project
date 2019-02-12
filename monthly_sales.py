# monthly_sales.py

# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

# File path = sales-201710.csv

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

import datetime as dt
import pandas as pd

import operator

#ALL Variables
top_sellers = []
total_monthly_sales = 0.0
individual_monthly_sales = 0.0
sales_price = 0.0


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
    top_sellers.append({"name": product_name, "monthly_sales": individual_monthly_sales})

top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse=True)


# print(top_sellers)


print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: " + str(total_monthly_sales))

print("Product               Sum of sales price")

    # matching_product = [p for p in products if p["id"] == selected_id]
    # product = matching_product[0]["name"]
    # matching_price = matching_product[0]["price"]


# matching_product = [p for p in products if p["product"] == "Khaki Pants"]

# print(matching_product["unit price"])

# for index, row in df.iterrows():
#     if row["product"] =="Khaki Pants":
#         print(row["sales price"] )

print("-----------------------")
print("TOP SELLING PRODUCTS:")

for p in top_sellers:
    print(p["name"] + "             " + str(p["monthly_sales"]))

print("-----------------------")
print("VISUALIZING THE DATA...")

# f= open("sales-201904.csv","r")
# print(f.read())

# TODO: make a chart

# adapted from code posted to matplotlib Slack channel: https://georgetown-opim-py.slack.com/archives/CFZDKNKA4/p1549494877005200

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

genres = []
viewers = []

for s in bar_data:
  genres.append(s["genre"])
  viewers.append(s["viewers"])

plt.bar(genres, viewers)
plt.ylabel("Viewers")
plt.xlabel("Genre")
plt.show()