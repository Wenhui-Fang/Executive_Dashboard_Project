# monthly_sales.py

# TODO: import some modules and/or packages here

# TODO: write some Python code here to produce the desired functionality...

# File path = sales-201710.csv

import matplotlib as plt
import datetime as dt
import pandas as pd
from matplotlib import style

#ALL Variables
top_sellers = []
total_sales = 0.0
individual_sales = 0.0
sales_price = 0.0
matching_product = " "

df = pd.read_csv("sales-201904.csv")

#Gettign unique 
products = df["product"].unique()

print(type(products))

print(products)

total_sales = df['sales price'].sum()

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: " + str(total_sales))

print("Product               Sum of sales price")

    # matching_product = [p for p in products if p["id"] == selected_id]
    # product = matching_product[0]["name"]
    # matching_price = matching_product[0]["price"]


matching_product = [p for p in products if p["product"] == "Khaki Pants"]

print(matching_product["unit price"])

# for index, row in df.iterrows():
#     if row["product"] =="Khaki Pants":
#         print(row["sales price"] )

print(individual_sales)

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")

print(df['unit price'][0])

# f= open("sales-201904.csv","r")
# print(f.read())