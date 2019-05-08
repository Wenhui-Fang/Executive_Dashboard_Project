# monthly_sales.py
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.ticker as ticker
import datetime as dt
import pandas as pd
import operator
import os
import calendar

#converting float to USD adapted from https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
def to_usd(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)

#adapted from https://github.com/s2t2/exec-dash-starter-py/pull/1/files
def top_selling_products(sales):
    all_products = sales.groupby(["product"]).sum()
    all_products = all_products.sort_values("sales price", ascending=False)
    top_products = []
    rank = 0
    for i, row in all_products.iterrows():
        d = {"rank": rank, "name": row.name, "monthly_sales": row["sales price"]}
        top_sellers.append(d)
        rank = rank + 1
    return top_products

if __name__ == "__main__":
  # OPTION B: prompt the user to input their selection.
  while True:
    datatype_pass = True
    range_pass = True
    program_pass = True
    year_month = input("Please enter the year and month for the data you want to view in a yyyymm format (e.g.: 201803)")

    #Input validation
    if not year_month.isdigit():
      print("INPUT DATA TYPE ERROR! Please only enter a specific year and month in a yyyymm format! Let's try again.")
      datatype_pass = False
    if datatype_pass == True:
      #I set a reasonable time frame for the sales to take place (between year 1900 and 2020)
      if int(year_month) not in range(190001,202012):
          print("Please ensure the year and month are reasonable values. Let's try again.")
          range_pass = False
      if range_pass ==True:    
          csv_filename = "sales-" + str(year_month) +".csv"
          csv_filepath = os.path.join("data/", csv_filename)

          #validation adapted from https://github.com/hiepnguyen034/data_dashboard/blob/master/exec_dash.py
          if not os.path.isfile(csv_filepath):
              program_pass = False
              #fail gracefully by: 1) displaying a friendly error message 
              # 2) avoiding runtime errors, and 3) preventing further execution.
              print("Sorry. The program cannot find a file at that location and will terminate now.")
              break
          else:
              break

  # create a bool variable to prevente further execution if validation fails
  if program_pass == True:
    
    top_sellers = []
    df = pd.read_csv(csv_filepath)
    total_monthly_sales = df['sales price'].sum()

    month = int(str(year_month)[4:6])
    #converting month number to name adapted from https://stackoverflow.com/questions/6557553/get-month-name-from-number
    month_name = dt.date(1900, month, 1).strftime('%B')
    year = int(str(year_month)[:4])

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

    print("-----------------------")
    print("MONTH: " + month_name + " " + str(year))
    print("-----------------------")
    print("CRUNCHING THE DATA...")
    print("-----------------------")
    print(f"TOTAL MONTHLY SALES:  {to_usd(total_monthly_sales)}")
    print("Product".ljust(18) + "Sum of sales price".rjust(15))
    print("-----------------------")
    print("TOP SELLING PRODUCTS:")

    for p in top_sellers:
        print(p["name"].ljust(18) + to_usd(p["monthly sales"]).rjust(15))

    print("-----------------------")
    print("VISUALIZING THE DATA...")

    # adapted from code posted to matplotlib Slack channel: https://georgetown-opim-py.slack.com/archives/CFZDKNKA4/p1549494877005200

    bar_data = top_sellers
    product_list = []
    sales_list = []

    for p in bar_data:
      product_list.append(p["name"])
      sales_list.append(round(p["monthly sales"],2))

    #Formatting adapted from https://github.com/s2t2/exec-dash-starter-py/blob/master/monthly_sales_alt.py#L77
    product_list.reverse()
    sales_list.reverse()
    fig, ax = plt.subplots() 

    #displaying x axis grid
    ax = plt.axes()        
    ax.xaxis.grid()

    #formating X axis ticker 
    #adapted from https://stackoverflow.com/questions/38152356/matplotlib-dollar-sign-with-thousands-comma-tick-labels
    fmt = '${x:,.0f}'
    tick = ticker.StrMethodFormatter(fmt)
    ax.xaxis.set_major_formatter(tick) 

    #Make the chart
    plt.barh(product_list,sales_list, align = "center", alpha=0.7)

    #displaying labels using a loop
    #adapted from https://www.reddit.com/r/learnpython/comments/2y9zwq/adding_value_labels_on_bars_in_a_matplotlib_bar/
    for a,b in zip(sales_list,product_list):
      plt.text(a, b, str(to_usd(a)))

    plt.ylabel("Products")
    plt.xlabel("Sales (USD)")
    plt.title("Top Selling Products " + "(" + month_name + str(year) + ")")
    plt.tight_layout()
    plt.show()