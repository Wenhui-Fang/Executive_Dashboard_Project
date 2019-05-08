from monthly_sales import to_usd
from monthly_sales import top_selling_products
import os
import pandas

def test_to_usd():
    assert to_usd(6.66) == "$6.66"
    assert to_usd(6) == "$6.00"
    assert to_usd(-6) == "-$6.00"

#adapted from https://github.com/s2t2/exec-dash-starter-py/pull/1/files
def test_top_selling_products():
    csv_filepath = os.path.join(os.path.dirname(__file__), "mock_data", "sales-201804.csv")
    sales = pandas.read_csv(csv_filepath)
    results = top_selling_products(sales)
    expected_result = [
        {'rank': 1, 'name': 'Button-Down Shirt', 'monthly_sales': 6374.90},
        {'rank': 2, 'name': 'Super Soft Hoodie', 'monthly_sales': 1950.00},
        {'rank': 3, 'name': 'Khaki Pants', 'monthly_sales': 1246.00},
        {'rank': 4, 'name': 'Vintage Logo Tee', 'monthly_sales': 1036.7500000000002},
        {'rank': 5, 'name': 'Sticker Pack', 'monthly_sales': 202.50},
        {'rank': 6, 'name': 'Baseball Cap', 'monthly_sales': 200.96999999999997},
        {'rank': 7, 'name': 'Brown Boots', 'monthly_sales': 125.00}
    ]
    assert results == expected_result